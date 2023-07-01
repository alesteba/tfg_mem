Es importante preparar un entorno común para el equipo. Django es un framework muy útil por la integración de las herramientas que hemos visto (ORM, integración continua (Jenkins), etc.), pero para conseguir un workflow adecuado necesitamos incluir otras herramientas propias de ciencia de datos como pueden ser cuadernos de jupyter y sus entornos, con las librerías necesarias para ejecutar modelos predictivos.

Jenkins es una herramienta de integración continua muy relevante para el proceso de automatización y mejora continua que queremos implantar. En este punto mencionamos cómo se incluye en la máquina Vagrant que contiene el proyecto. En los siguientes puntos veremos cómo permite integrar los distintos scripts de carga de datos junto con la generación de la vista minable y posterior modelo que conformar el pipeline que queremos conseguir.

Dedicamos varios días a preparar la integración de Django con cuadernos jupyter y a ejecutar diferentes entornos virtuales con las librerías adecuadas en cada momento. Los siguientes ejemplos muestran cómo se ha conseguido integrar las librerías necesarias para el despliegue de los cuadernos y su integración con los datos y los modelos de Django.

```python

# base code for jupyter integration

import sys, os, django

BASE_DIR = os.path.dirname(os.path.abspath('../../agrai/'))

sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agrai.settings")

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

django.setup()

```

Los cuadernos jupyter que se encuentran en esta memoria se han exportado desde la propia aplicación. Vemos la facilidad con la que el equipo puede redactar informes para clientes concretos, utilizando los datos de la aplicación directamente.  El código anterior es el 'snippet' necesario para poder integrar los cuadernos con las llamadas concretas a los modelos de Django. Estos cuadernos son un punto tan importante de la arquitectura como puede ser el módulo de servicios.

