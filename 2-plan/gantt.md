
El siguiente diagrama propone un desglose de tareas para la planificación del proyecto. El tiempo estipulado es de dos meses y una semana.

```mermaid
gantt
    title Planificación
    dateFormat  DD-MM
    axisFormat  %d
    
	section ANALISIS
    ALCANCE: 01-01, 2d
    METODOLOGIA: 02-01, 3d
	EDT: 03-01, 5d
	GANNT: 04-01, 5d
    RRHH: 05-01, 3d
    COMUNICACIONES: 06-01, 5d
	RIESGOS: 07-01, 5d
	
	section INFRAESTRUCTURA
    DJANGO+JUPYTER: 08-01, 3d
    SCRIPT_.SH: 09-01, 4d
    
	section MODELO_DATOS
    RELACIONES BD: 10-01, 20d
    REDISEÑO: crit, 11-01, 20d
    
	section PIPELINE
    BLOQUES:  30-01, 10d
    FEATURES: 05-02, 5d
    VISTA: 05-02, 5d
    
    section MODELO_PRODUCCIÓN
    LOAD: 10-02, 5d
    VIEW: 11-02, 5d
	REGRESSION: 12-02, 10d
    BEST_MODEL: 15-02, 10d
    
    section TEST
    TEST 1: 20-01, 30d
    TEST 2: 30-01, 30d
    Phase 3 complete: milestone, 01-03, 0d

	section MEMORIA
	MEM_WRITE: 01-01, 60d
    SEG_Y_CONT: 01-01, 60d
	
    Project complete: milestone, 10-03, 0d
```

Este diagrama es una estipulación de cómo se desarrolla el proyecto. En la sección final de seguimiento y control analizamos las desviaciones encontradas y cómo han sido solucionados estos contratiempos.

Destacamos que las tareas de escritura de la memoria y pruebas unitarias se realizan durante casi todo el proyecto. Las pruebas nos permiten asegurarnos de que el proyecto funciona adecuadamente: así no pasamos a una nueva tarea si no hemos dejado la aplicación estable al terminar la anterior.