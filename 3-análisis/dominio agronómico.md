Una vez en contexto, procedemos a justificar las decisiones de diseño que la aplicación AGRAI necesita para llegar al rediseño que hemos identificado como clave.

AGRAI es una aplicación para la gestión de cultivo que permite al agricultor monitorizar el estado de sus parcelas. El estado actual de la aplicación se centra el despliegue de datos georreferenciados por medio de una interfaz web. Los resultados para el usuario de la aplicación son satisfactorios, permitiendo a éste consultar el estado de su parcelario junto con algunas predicciones en cualquier momento. 

Tenemos que situarnos en el uso que se le está dando a la aplicación en relación con el diseño de ésta. La monitorización efectuada es válida para cualquier tipo de cultivo susceptible de ser fotografiado desde una imagen satelital y/o de dron. El modelo de datos que utiliza, aunque pobre al comienzo del trabajo, permite registrar tantos cultivos como un potencial cliente desee. Por otro lado, el caso real de uso de la aplicación proviene de bodegas o cooperativas vitivinícolas que quieren predecir la cantidad de kg de cosecha en una campaña determinada (2020-2021).

Como punto de partida buscaremos identificar las entidades del dominio necesarias para que nuestro nuevo modelo de datos represente y relacione toda la información con precisión.

En la interfaz web, el cliente observa un mapa con sus parcelas resaltadas en colores. Este color reflejado en los píxeles hace referencia a los índices vegetativos provenientes de las imágenes satelitales. Los clientes utilizan dicha interfaz para ver el estado de sus cultivos y observar la producción que predicen los modelos de Inteligencia Artificial generados.

![](figures/visor_GIS.png)

A nivel interno, el equipo trabaja con datos provenientes de imágenes descargadas de satélites como SENTINEL, o de grabaciones realizadas por dron cuando se requiere una mayor calidad. Estos datos se mezclan con información proporcionada por estaciones meteorológicas como el SIAR y con la información que los clientes pueden proporcionar sobre campañas anteriores.

Por otro lado, el proceso actual de esta información es tedioso para el equipo. Los diferentes miembros trabajan con tecnologías distintas sobre datos, muchas veces duplicados, que provienen de fuentes comunes. Los requisitos que identificamos en el siguiente punto consideran la idea de optimización continua necesaria.

![caption](figures/lean.png)




