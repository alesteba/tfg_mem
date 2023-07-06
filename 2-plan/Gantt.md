
El siguiente diagrama propone un desglose de tareas para la planificación del proyecto. Este diagrama es una estipulación de cómo se desarrolla el proyecto. En la sección final de seguimiento y control analizamos las desviaciones encontradas y cómo han sido solucionados estos contratiempos.

```mermaid
gantt
    title Planificación
    dateFormat  DD-MM
    axisFormat  %d
    
	section ANALISIS
    ANALISIS: 01-01, 10d
	
	section INFRAESTRUCTURA
    ARQUITECT : 10-01, 10d
    VAGRANT: 10-01, 10d
    ENTORNO: 10-01, 10d
    
	section DATOS
    RELACIONES BD: 10-01, 20d
    REDISEÑO: crit, 10-01, 20d
    
	section PIPELINE
    BLOQUES: 30-01, 10d
    SCRIPT: 04-02, 8d
    JENKINS: 04-02, 8d
    
    section MODELO
    LOAD: 10-02, 5d
    VIEW: 10-02, 10d
	REGRESSION: 10-02, 10d
    BEST_MODEL: crit, 15-02, 15d

	section MEMORIA
	MEM_WRITE: 01-01, 70d
    SEG_Y_CONT: 01-01, 70d
```

Destacamos que las tareas de escritura de la memoria y pruebas unitarias se realizan durante casi todo el proyecto. Las pruebas nos permiten asegurarnos de que el proyecto funciona adecuadamente: así no pasamos a una nueva tarea si no hemos dejado la aplicación estable al terminar la anterior.