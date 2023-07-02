
El siguiente diagrama propone un desglose de tareas para la planificación del proyecto. El tiempo estipulado es de dos meses y una semana.

```mermaid
gantt
    title Planificación
    dateFormat  DD-MM
    axisFormat  %d
    
	section ANALISIS
    ANALISIS: 01-01, 10d
	
	section INFRAESTRUCTURA
    ARQUITECTURA: 10-01, 50d
    VAGRANT: 10-01, 10d
    ENTORNO: 10-01, 10d
    
	section DATOS
    RELACIONES BD: 10-01, 20d
    REDISEÑO: crit, 10-01, 20d
    
	section PIPELINE
    BLOQUES:  30-01, 10d
    SCRIPT: 05-02, 5d
    VISTA: 05-02, 5d
    
    section MODELO
    LOAD: 10-02, 5d
    VIEW: 11-02, 5d
	REGRESSION: 12-02, 10d
    BEST_MODEL: crit, 15-02, 10d

	section MEMORIA
	MEM_WRITE: 01-01, 60d
    SEG_Y_CONT: 01-01, 60d
	
    Project complete: milestone, 10-03, 0d
```

Este diagrama es una estipulación de cómo se desarrolla el proyecto. En la sección final de seguimiento y control analizamos las desviaciones encontradas y cómo han sido solucionados estos contratiempos.

Destacamos que las tareas de escritura de la memoria y pruebas unitarias se realizan durante casi todo el proyecto. Las pruebas nos permiten asegurarnos de que el proyecto funciona adecuadamente: así no pasamos a una nueva tarea si no hemos dejado la aplicación estable al terminar la anterior.