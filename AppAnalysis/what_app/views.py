from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Files
from auth_manage.models import Users
import pandas as pd
import os

def whatsapp_home(request):
    user_name = request.POST.get('user_name')
    chat_data = None  # Variable para almacenar los datos procesados

    if user_name:
        # Guardamos el 'user_name' en la sesión si se recibe en GET
        request.session['user_name'] = user_name
    else:
        # Si no está en la URL, lo obtenemos de la sesión
        user_name = request.session.get('user_name')
    
    if not user_name:  # 🛑 Si user_name sigue siendo None, redirigir o mostrar un mensaje
        messages.error(request, "Debes ingresar un usuario válido.")
        print('No entro')
        return redirect('login')  # Asegúrate de que la URL de 'login' existe

    if user_name:
        try:
            user = Users.objects.get(user_name=user_name)
        except Users.DoesNotExist:
            messages.error(request, 'Usuario no válido.')
            return redirect('login')

        # Manejar subida y análisis del archivo
        if request.method == 'POST' and 'archivo' in request.FILES:
            file = request.FILES['archivo']
            try:
                # Guardar el archivo en la base de datos
                new_file = Files(file=file, user_name=user)
                new_file.save()
                messages.success(request, 'Archivo subido correctamente.')

                # Procesar el archivo inmediatamente
                try:
                    with open(new_file.file.path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    chat_data = parse_whatsapp_content(content)  # Función de análisis
                except Exception as e:
                    messages.error(request, f'Error al leer el archivo: {str(e)}')

            except Exception as e:
                messages.error(request, f'Error al guardar el archivo: {str(e)}')

        # Obtener el último archivo subido (si no se subió uno nuevo)
        if not chat_data:
            try:
                latest_file = Files.objects.filter(user_name=user).latest('uploaded_at')
                with open(latest_file.file.path, 'r', encoding='utf-8') as f:
                    content = f.read()
                chat_data = parse_whatsapp_content(content)
            except Files.DoesNotExist:
                messages.info(request, 'No hay archivos subidos para analizar.')
            except Exception as e:
                messages.error(request, f'Error al procesar el archivo: {str(e)}')

        return render(request, 'what.html', {
            'user_name': user_name,
            'chat_data': chat_data  # Enviar datos al template
        })





def parse_whatsapp_content(content):
    entries = []
    # Dividir el contenido en líneas y limpiar espacios
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    for line in lines:
        # Dividir fecha/hora del resto (solo en la primera ocurrencia de '-')
        if '-' in line:
            parts = line.split('-', 1)  # Split en la primera ocurrencia
            date_time = parts[0].strip()
            
            # Dividir remitente y mensaje (solo en la primera ocurrencia de ':')
            if ':' in parts[1]:
                sender, message = parts[1].split(':', 1)
                entries.append({
                    'Fecha': date_time,
                    'Remitente': sender.strip(),
                    'Mensaje': message.strip()
                })
    
    # Crear DataFrame para análisis adicional (opcional)
    df = pd.DataFrame(entries)
    
    # Convertir a lista de diccionarios para la plantilla
    return df.to_dict('records')