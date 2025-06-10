# coderhouse-srpttProyecto Django: Blog de Componentes de PC
Este proyecto es un blog hecho con Django, donde podes administrar info sobre componentes de PC como procesadores, motherboards y tarjetas gráficas.
----
Tiene tres modelos diferentes para cada componente, formularios para crear nuevos datos en cada uno, y un formulario para buscar procesadores por nombre (la búsqueda no está para todos los modelos, solo para ese).
----
Usa herencia de plantillas HTML para que no tengas que repetir código en cada página, con una plantilla base que se extiende.
----
Qué hay en el proyecto
blogpc/: la carpeta del proyecto principal de Django
---
componentes/: la app donde están los modelos, vistas, y formularios
---
templates/: acá están las plantillas HTML, con base.html y las otras páginas que extienden de esta
---
static/: archivos estáticos, como CSS o imágenes
----
Modelos que cree
Procesador: tiene nombre, cantidad de núcleos y frecuencia
TarjetaGrafica: nombre, memoria y fabricante
PlacaMadre: nombre, chipset y socket
---
Cómo usarlo?
Clonar el repo y entrar a la carpeta
---
git clone <https://github.com/LucasP0tato/coderhouse-srptt>
cd blogpc
Crear un entorno virtual y activar
---
python -m venv venv
source venv/bin/activate  # o en windows: venv\Scripts\activate
Instalar Django
---
pip install django
Migrar la base de datos
---
python manage.py migrate
Arrancar el servidor
---
python manage.py runserver
Abrir en el navegador:
---
cpp
Qué podés hacer
-Crear nuevos procesadores, placas madre y tarjetas gráficas con formularios
-Buscar procesadores por nombre y ver resultados
-Navegar las distintas páginas con el menú que usa la plantilla base
--------
Algunas cosas para tener en cuenta
-El admin.py está vacío, si querés podes agregar los modelos para manejar todo desde el admin de Django (pero no está hecho acá)
-Las carpetas migrations están vacías al principio, pero se llenan cuando migrás
-La herencia de templates ayuda a que no tengas que repetir el mismo código HTML en todas las páginas