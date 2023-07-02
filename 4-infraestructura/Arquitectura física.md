
El entorno local, sobre el cual desarrollamos, y el de producción, donde se despliega la aplicación, son actualmente diferentes. Todos los miembros del equipo utilizamos máquinas Windows, mientras que en el servidor de producción encontramos una máquina Ubuntu. Esto crea un problema importante en el proceso de instalación de las librerías necesarias para trabajar con los datos; se pierde gran cantidad de tiempo en preparar el entorno de cada persona que va a trabajar con el repositorio de la aplicación; además, las librerías necesarias necesitan de una gran cantidad de dependencias que varían en cuanto a las versiones. Como solución propondremos una nueva forma de trabajo que nos asegure un entorno común con las mismas librerías y paquetes.

Parte del trabajo consiste en la automatización del despliegue de la aplicación. En este punto veremos cómo la infraestructura como código permite aislar las librerías necesarias creando un script que deja una máquina en estado estable para ejecutar la aplicación. Para poder utilizar tecnologías que posibiliten la integración continua, transformamos el entorno de desarrollo desplegando la aplicación en UNIX mediante una máquina virtual Vagrant en la que podamos reproducir varias veces el proceso. Identificamos las siguientes dependencias que necesitan ser instaladas:

- Postgres 14 + Postgis
- Python3.10
- GDAL 3.3.2
- Django
- Jenkins

Suele ser complicado encontrar todas las dependencias con sus versiones correctas; en este caso el punto más complicado ha sido la instalación de Python con su versión correspondiente de GDAL, librería que permite tratar con los datos geoespaciales. Además, el sistema gestor de BD, 'postgres', necesita una extensión especial, 'postgis', para poder guardar los datos georreferenciados. Como este tipo de trabajo es casi de prueba y error, la utilidad del script que obtenemos es de gran valor.

Jenkins es una herramienta de integración continua muy relevante para el proceso de automatización y mejora continua que queremos implantar. Aquí mencionamos cómo se incluye en la máquina Vagrant que contiene el proyecto. En los siguientes puntos veremos cómo permite integrar los distintos scripts de carga de datos junto con la generación de la vista minable y posterior modelo que conformar el pipeline que queremos conseguir.
