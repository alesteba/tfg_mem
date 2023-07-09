El código de la aplicación que heredamos está escrito en Python. El lenguaje es una decisión adecuada debido a la necesidad de integrar técnicas de procesamiento de datos e inteligencia artificial. El framework de Django para Python permite construir un proyecto robusto y desplegarlo en un servidor con una interfaz web.

*Django* nos ofrece las herramientas necesarias para trabajar desde un alto nivel de abstracción y poder diseñar una aplicación sólida y estable. Algunas de estas herramientas son:

- ORM, Object-Relational-Mapping: permite crear un modelo de datos y gestiona automáticamente la BD (base de datos) subyacente. Abstrae las consultas SQL y evita tener que realizar migraciones manuales de los esquemas.
- Static File Generator: podemos diseñar la interfaz de la aplicación en formato web y desplegar en un servidor.
- Commands-System: gestión de comandos internos mediante los que se puede automatizar tareas; utilizaremos esta arquitectura para diseñar el pipeline de datos y almacenar la información proveniente de diferentes fuentes.

![Ejemplo de uso de un comando en Django para ejecutar la descarga de los índices (salida del comando mostrada en Jenkins).](figures/django-commands.png)

Aunque el framework es muy potente, harán falta otras herramientas y entornos para completar con éxito la automatización que buscamos para así conseguir un proceso de optimización continua. En el siguiente punto hablaremos de la infraestructura que la aplicación requiere y de cómo podemos solventar algunos de los problemas de integración más importantes. Mencionamos algunas de estas tecnologías:

- Vagrant: virtualización de una máquina Unix en la que podamos provisionar el proyecto y reproducir los pasos necesarios de nuestro pipeline.
- Jenkins: herramienta de integración continua que permite declarar un pipeline a modo de infraestructura como código. 

La utilización de *Python*, aparte de incluir el framework de Django, nos da la posibilidad de utilizar las librerías de inteligencia artificial y ciencia de datos que son necesarias para la creación del modelo de producción de cultivo. Algunas de librerías principales que vamos a utilizar son las siguientes:

LIBRERÍA | DESCRIPCIÓN
:----------------|:-------------:
scikit-learn | Creación de modelos de inteligencia artificial
numpy | Tratamiento de datos multidimensionales
pandas | Uso de datos tabulados con herramientas para su procesamiento
jupyter | Integración de cuadernos procesables con el resto del proyecto



