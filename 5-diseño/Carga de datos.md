Un modelo claro y robusto va a permitir cargar datos en la aplicación de forma ordenada con posibilidad de ser escalados en el futuro. En la implementación del pipeline que veremos en siguientes apartados haremos hincapié en los estados de carga por los que pasan los datos; de momento solo importa destacar que el modelo actual permite mantener un histórico de datos mucho más sólido que el que estaba implantado cuando comenzamos el desarrollo. 

Es importante explicar por qué vamos a poner tanto énfasis en que estos datos se gestionen de manera fluida y eficaz. La interfaz web de la aplicación muestra la punta de un iceberg en la que el usuario observa las parcelas coloreadas basándose en los índices vegetativos, también se muestra la producción estimada.

![Ejecución del pipeline mientras realiza la descarga de datos del satélite Copernicus.](figures/load.png)

El proceso de carga de datos hace uso de un módulo de descarga de imágenes satelitales que obtiene el valor de estos índices vegetativos. Este script de descarga ha sido desarrollado por el equipo y ha sido colocado dentro del módulo de automatización junto con otras tareas similares. Utilizaremos el módulo como una caja negra y aseguraremos el correcto uso de este para que los índices vegetativos terminen en sus tablas correspondientes dentro de la BD.

Los índices que renderiza el visor de la aplicación son el resultado de todo el proceso que estamos exponiendo. Es el punto más delicado que requiere del diseño de varias entidades para guardar un histórico de datos. En la visualización del histórico de índices vegetativos es el mayor valor que obtiene el cliente cuando accede a la aplicación.
