
El siguiente diagrama propone un desglose de tareas para la planificación del proyecto. Este diagrama es una estipulación de cómo se desarrolla el proyecto, en el eje horizontal, medimos el tiempo en días. Considerando 4 h de trabajo diarias, obtenemos una duración de 75 días para repartir las 300 h a lo largo de los próximos 6 meses que podemos dedicarle al trabajo. En la sección final de seguimiento y control analizamos las desviaciones encontradas y cómo han sido solucionados estos contratiempos.

```mermaid
gantt
    title Planificación
    dateFormat  DDD
    axisFormat  %j
    
	section ANALISIS
    ANALISIS: 01, 10d
	
	section INFRAESTRUCTURA
    ARQUITECT : 10, 10d
    VAGRANT: 10, 10d
    ENTORNO: 10, 10d
    
	section DATOS
    RELACIONES BD: 20, 15d
    REDISEÑO: crit, 20, 15d
    
	section PIPELINE
    BLOQUES: 35, 10d
    SCRIPT: 37, 8d
    JENKINS: 37, 8d
    
    section MODELO
    LOAD: 45, 5d
    VIEW: 45, 10d
	REGRESSION: 45, 15d
    BEST_MODEL: crit, 55, 15d

	section MEMORIA
	MEM_WRITE: 20, 56d
    SEG_Y_CONT: 01, 75d
```

Destacamos que las tareas de escritura de la memoria y pruebas unitarias se realizan durante casi todo el proyecto. Las pruebas nos permiten asegurarnos de que el proyecto funciona adecuadamente: así no pasamos a una nueva tarea si no hemos dejado la aplicación estable al terminar la anterior.