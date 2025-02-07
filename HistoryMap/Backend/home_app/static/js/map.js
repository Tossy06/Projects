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

    function alert(){
        alert('Se hiwo click en el mapa')
    }

    createHistory.addEventListener('click', mostrarForm);
    cancelar.addEventListener('click', ocultar);

    let foliumMap = document.querySelector('.folium-map')
    if (!foliumMap) {
        console.error("No se encontró el mapa de Folium.");
        return;
    }
    else{
        console.log('se cargo')
    }

    // Esperamos un poco para asegurarnos de que el mapa de Leaflet está inicializado
    setTimeout(() => {
        let mapElement = foliumMap.querySelector("iframe");
        if (!mapElement) {
            console.error("No se encontró el iframe del mapa.");
            return;
        }
        else{
            console.log('Se cargo el iframe')
        }

        // Accedemos al contenido del iframe
        let mapDoc = mapElement.contentDocument || mapElement.contentWindow.document;

        // Buscamos la capa del mapa de Leaflet
        let leafletMap = mapDoc.querySelector(".leaflet-container");
        if (!leafletMap) {
            console.error("No se encontró la capa de Leaflet.");
            return;
        }
        else{
            console.log('Se ecnotro la capa leaf')
        }

        console.log("Mapa de Folium detectado. Listo para capturar clics.");

        // Agregar evento de clic
        leafletMap.addEventListener("click", function (event) {
            // Aseguramos que el evento tenga las coordenadas latlng
            if (event.latlng) {
                const lat = event.latlng.lat;
                const lng = event.latlng.lng;

                // Mostrar las coordenadas en la consola o asignarlas a los campos del formulario
                console.log(`Coordenadas: Latitud: ${lat}, Longitud: ${lng}`);

                // Aquí puedes llenar los campos del formulario con las coordenadas
                document.getElementById('latitud').value = lat;
                document.getElementById('longitud').value = lng;

                // Mostrar el formulario
                mostrarForm();
            } else {
                console.error("No se encontraron las coordenadas del evento.");
            }
        });

        
    }, 1000); // Pequeño delay para asegurar la carga

    
    
    }
)
