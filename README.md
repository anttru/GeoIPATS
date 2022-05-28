# Gelolocalizador ATS

Este programa requiere los módulos IPy y tkintermapview que pueden instalarse con PIP, en Windows es suficiente con estos dos y Python3, en linux necesita además PIL, para mas detalles se puede consutlar el archivo installation.
La entrada acepta IPsv4 de tipo público o URLS. Puede seleccionarse el número máximo de routers con los que se intentará contactar (hops) y el tiempo de espera para cada uno de los tres intentos de contacto con cada uno de ellos ( timeout) en un menú desplegable.
Se mostrará la ruta en el mapa y un menú para seleccionar las ips y ver sus datos.
Con el boton borrar se puede limpiar el mapa y los datos de IPs guardados. Se limpiarán también al realizar una nueva búsqueda.

El programa se ejecuta ejecutando GeoIPATS.py con el intérprete de Python. En linux necesitará permisos de administrador para funcionar correctamente (sudo python3 GeoIPATS.py).

Para un uso más fácil, puede descargarse esta versión que trae todos los requisitos:

Windows: 
Linux:

Puede hacerse uso de las funciones del modelo instanciando un modelo y usando sus métodos directamente. 

