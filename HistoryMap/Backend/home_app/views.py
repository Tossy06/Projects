from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stories
from usermanage_app.models import Users
import folium
from folium.plugins import MousePosition
from folium.utilities import JsCode


# Create your views here.
def home(request):
    user_name = request.POST.get('user_name')

    if user_name:
        # Guardamos el 'user_name' en la sesión si se recibe en GET
        request.session['user_name'] = user_name
    else:
        # Si no está en la URL, lo obtenemos de la sesión
        user_name = request.session.get('user_name')
    
    if user_name:
        try:
            user = Users.objects.get(user_name = user_name)
        except Users.DoesNotExist:
            messages.error(request, 'El usuario no existe.')
            return redirect('register-login')

        # Guarda el mapa como HTML
        mapa_html = generar_mapa()
        # Combina los datos en un único diccionario
        context = {
            'mapa': mapa_html,
            'user_name': user_name
        }


    
        if request.method == 'POST':
            history_name = request.POST.get('history_name')
            descripcion = request.POST.get('descripcion')
            latitud = request.POST.get('latitud')
            longitud = request.POST.get('longitud')

            try:
                new_history = Stories(history_name = history_name, descripcion = descripcion, latitud = latitud, longitud = longitud, user_name = user)
                new_history.save()
                print('Se guardooo')
                messages.success(request, 'Nota agregada con éxito')
                return redirect('home')
            
            except Exception as e:
                messages.error(request, f'Error al guardar la nota: {e}')
                print(f'Error: {e}')
    
        return render(request, 'home.html', context)

    # Si no hay `user_name`, renderiza un template sin mapa
    return render(request, 'auth.html', {'user_name': None})

def generar_mapa():
    #Localización inicial
    location = [0, 0]
    # Crea un mapa centrado en una ubicación (ejemplo: Bogotá, Colombia)
    mapa = folium.Map(
        location=location, 
        zoom_start=3,
        min_zoom=2, 
        tiles="CartoDB Dark_Matter",
        no_wrap=True,
        max_bounds=True, 
        control_scale=True
    )
    mapa.add_child(
        folium.LatLngPopup()
    )

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' &deg; ';};"

    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(mapa)

    
    # Agrega un marcador al mapa
    stories = Stories.objects.all()
    for story in stories:
        location = [story.latitud, story.longitud]
        folium.Marker(
            location=location,
            popup=folium.Popup(f"<b>{story.history_name}</b><br>{story.descripcion}", max_width=300),
            icon=folium.Icon(color="green", icon="info-sign")
        ).add_to(mapa)

    return mapa._repr_html_()