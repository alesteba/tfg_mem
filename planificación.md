esto sobra

- INTRODUCCIÓN

	- Antecedentes [[justificación]]

- PLANIFICACIÓN

	- Alcance [[alcance]]
	- Metodologia [[metodología]]
	- EDT [[EDT]]
	- Entregables [[entregables]]
	- Tiempos [[tiempos]]
	- GANTT [[gantt]]
	- Recursos Humanos [[rrhh]]
	- Plan de comunicaciones [[comunicaciones]]
	- Análisis de Riesgos [[riegos]]

- ANÁLISIS

	- Discusión Pipeline (Reuninones)
	- Revisión de la Estructura del diseño anterior.
	- Explicación Diseño

- DISEÑO (entregables)

	- Explicación Diseño Actual
	- Estructura Excel Datos de Entrada (snippet)
	- Preprocesamiento Datos 
	- Diseño Vista Minable

- TAREAS

	- Modelo de Datos
		- Transformación de datos + Justificación de features
		- DOC datos entrada
	- Entorno
		- herramientas integración continua equipo
		- Django + jupyter notebooks.
	- Implementación pipeline
		- infraestructura
			- Entorno Linux + automatización .sh
			- Instalación en varias máquinas
		- carga de datos Inicial (1S)
		- selección de características
		- transformación de datos
		- obtención vista minable
		- implementación modelo de producción de cultivo
		- visualización resultados en la interfaz
	- Implementación modelo Producción
	- Pipeline Jenkins (automatización de la instalación de la applicacion y despliegue) _> solo si llego.
	- Depliegue de la interfaz (esta preparada ¿?)

- TEST Y PRUEBAS

	- Integración de nuevos datos para la aplicación y comprobación del correcto funcionamiento de los modelos.
	- Prueba del código en BD de forma paralela. (durante todo el desarrollo de la aplicación)

- MEMORIA

	- Redacción de Memoria (20 h)

- SEGUIMIENTO Y CONTROL (MANTENIMIENTO)

	- observación del nuevo flujo de trabajo a partir del rediseño de software.
	- durante de todo el proyecto (sin estipular)
	- varias pruebas de carga de datos