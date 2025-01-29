document.addEventListener('DOMContentLoaded', function (){
    const cancelar = document.getElementById('cancel-button');
    const form = document.getElementById('story-form');
    const createHistory = document.getElementById('create-History'); // Mejor nombre de variable
    form.style.display = 'none';
    function mostrarForm(){
        form.style.display = 'flex';
        form.scrollIntoView({ behavior: 'smooth' });
    }

    function ocultar(){
        form.style.display = 'none';
        
    }

    // Escuchar mensajes del mapa
    window.addEventListener('message', function(event) {
        if (event.data.type === 'mapClick') {
            document.getElementById('latitud').value = event.data.lat;
            document.getElementById('longitud').value = event.data.lng;
            mostrarForm();
        }
    });

    createHistory.addEventListener('click', mostrarForm);
    cancelar.addEventListener('click', ocultar);
    
    }
)
