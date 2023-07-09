Mencionábamos la búsqueda de optimización del proceso como una de las principales ideas para mejorar el flujo de datos que utiliza la aplicación. El rediseño que se quiere implantar y la arquitectura resultante tienen que cumplir con los principios de dicha metodología. Para que este trabajo resulte satisfactorio, el software tiene que poder utilizarse por el equipo con agilidad, consiguiendo que quede como una herramienta física que coordine bien todas las tareas de los participantes que la usan.

Para poder realizar este proyecto decidimos trabajar con un número pequeño representativo de datos de la aplicación, actualmente en producción. Un menor volumen de información permite realizar pruebas y da pie a fijarnos en las relaciones y los esquemas estructurales con más precisión.  
  
Como estamos buscando una optimización continua, a medida que voy haciendo pruebas con mi entorno local, un compañero se encarga de utilizar el mismo proyecto con volúmenes mayores de datos, que la aplicación utiliza en producción. La reestructuración del modelo de BD que realizamos contempla un posterior escalado de la aplicación que permitirá la integración continua con más datos y nuevas tecnologías.

La siguiente tabla muestra las principales fuentes de datos de las que se obtienen y enlaza la información. El volumen de datos que se puede llegar a manejar es grande ya que por cada parcela se almacenan varios índices vegetativos en cada uno de sus píxeles. 

FUENTE DATOS | DESCRIPCIÓN
:----------------|:-------------:
QGIS | Información geomométrica de parcelas y sus pixéles
Índices Vegetativos | Información provenientes de imágenes satelitales descargadas en diferentes fechas
Cultivos / Variedad | Información tabulada en excels sobre tipo de cultivos y sus variedades

Para poder realizar el trabajo utilizaremos, por tanto, una muestra representativa de los datos debido a que el proceso de descarga de índices y persistencia de datos es largo para realizar las pruebas. El sistema está pensado para trabajar con muchas parcelas; en las pruebas que yo voy a realizar escogemos una muestra de 25 parcelas y pensaremos una descarga de índices para no más de 4 fechas diferentes.

Para hacernos una idea, contemplando solo 25 parcelas, podemos almacenar 3000 píxeles. Por cada pixel vamos a registrar varios índices vegetativos (ndvi, ndre) y para generar el histórico de datos esta información se multiplica por el número de fechas contempladas. Es decir, que aunque trabajamos sobre un volumen reducido para probar la automatización, sigue siendo mucha la información que tiene que almacenarse en la base de datos.

Es el histórico de índices en diferentes fechas lo que permite al sistema realizar modelos predictivos. A mayor volumen de datos, más precisión podremos obtener en los modelos posteriormente. El punto importante de este trabajo es la mejora del proceso y la automatización del flujo de datos; ello nos llevará a que finalmente podamos obtener un modelo de regresión para predecir los kg de cultivo, tal y como el agricultor necesita. La muestra que utilizamos, al ser representativa con 25 parcelas, predecirá con un cierto sobreajuste a los datos. Por tanto nuestro esfuerzo se centra en que el proceso que implantamos sea reproducible para cualquier volumen de datos, y en que sin desarrollo adicional podamos utilizar el mismo proceso para predecir en el volumen que queramos.
