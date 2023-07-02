Esta memoria se incluye como un entregable del proyecto debido a las explicaciones y esquemas que contiene (principalmente para el modelo relacional). Para poder mejorar el flujo de trabajo, ciertos conceptos necesitan ser entendidos por los desarrolladores. La documentación aquí expuesta tiene un gran valor por el lenguaje ubicuo que implanta en el proyecto. 

El documento se ha escrito como notas en *markdown* por la facilidad que da para incluir fragmentos de código relativos al proyecto y poder explicar decisiones y conceptos. Para integrar los diagramas expuestos utilizamos tecnologías como *mermaid*, que posibilita editar los diagramas directamente en el documento, algo totalmente necesario cuando estos modelos se modifican a medida que avanzamos.

Finalmente, exportamos las notas en el orden necesario para la memoria y renderizamos el documento en html. El fácil acceso al documento tiene bastante relevancia por el uso que el equipo puede darle al consultar la documentación, especialmente la del modelo relacional y los servicios.

Utilizamos algunas herramientas de integración continua como Github Actions para automatizar este proceso. En un primer lugar convertimos el grafo de notas Markdown a un documento HTML mediante un proceso recursivo que ordena las notas y genera así la memoria del proyecto. Además, el índice se crea a partir de los nombres de las notas y sus relaciones con las que están enlazadas.

![](figures/graph.png)


Estas notas se encuentran en un repositorio separado al proyecto para poder así construir la memoria. Utilizamos Github Actions para definir las acciones necesarias cuando se realicen cambios en el repositirio, es decir, a medida que escribimos en las notas. En primer lugar, queremos conseguir que el documento se renderice cuando se hacen cambios en el repositorio y se publique posteriormente dicha memoria en una pequeña web bajo el dominio asociado a nuestro usuario de Github Pages. En segundo lugar, una vez tenemos publicada la memoria, una segunda acción convertirá el código HTML asociado al documento en el archivo PDF que está leyendo actualmente. 

CODIGO ACTIONS: 