
--> explicación vagrant: 

Hacemos uso de WSL (Windows Subsystem for Linux) para crear el entorno de desarrollo necesario para el proyecto. De esta forma conseguimos que los entornos de pruebas y producción sean muy similares, permitiendo automatizar el despliegue de la aplicación mediante técnicas de infraestructura como código. Una de las ventajas de tener una máquina Ubuntu como entorno de desarrollo es que mediante un script .sh instalamos todas las dependencias necesarias para dejar dicha máquina lista para el despliegue de la aplicación.

Para el trabajo interno de la aplicación necesitamos entornos con librerías más pesadas como numpy o scikit-learn que no deberíamos usar en la producción de la interfaz web, ya que ésta simplemente muestra los datos del parcelario registrado con su producción estimada. Consideramos la posibilidad de crear varios entornos virtuales para los diferentes flujos de trabajo que contempla la aplicación.

- Despliegue de la información de la aplicación mediante interfaz
- Técnicas de ciencia de datos para la creación de modelos a nivel interno, backend.

Actualmente, solo existe un entono virtual sobre el cual se instalan todas las librerías *Python* necesarias para el desarrollo y despliegue. Dicha refactorización sobre la infraestructura se contempla para próximos hitos en el proyecto. Es importante identificar aquellos puntos que sean propensos a un *refactor* grande, pero que no se lleven a cabo en el momento actual. Una vez identificados, valoramos su importancia y vemos si el diseño actual impediría su mejora. En este caso sería muy sencillo, una vez crezca la aplicación, separar los entornos virtuales para mejorar el tiempo de compilación y despliegue.