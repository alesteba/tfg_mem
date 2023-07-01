
Como los datos con los que trabajamos en los cuadernos provienen de una base de datos estructurada y previamente estudiada, no va a hacer falta un paso de preprocesamiento previo. De todas formas, sí que intentaremos que los datos de producción con los que vamos a predecir estén normalizados y que se haya hecho una búsqueda previa de 'outliers'.

Buscamos un modelo de regresión para el número de Kg de cultivo en cada parcela. Aunque los datos son representativos de un parcelario pequeño, diseñaremos los cuadernos para automatizar la búsqueda del mejor modelo con cualquier volumen de datos que podamos necesitar más adelante.

El rango de valores para la mayoría de los índices que obtenemos va de -1 a 1. Los datos de índices negativos que llegan a la vista se pueden considerar como 'outliers'. Esto es debido a que, si los índices provienen de una imagen con nubes, no se diferencian los colores del terreno y el índice acaba teniendo un valor muy malo. Para evitar valores corruptos eliminaremos los índices que provengan de la toma de la imagen en una fecha en la que había nubes.

![](figures/nubes.png)

El [siguiente repositorio](https://github.com/alesteba/tfg/tree/main/entregables) contiene los cuadernos necesarios para la gestión y automatización de los modelos de producción generados a partir los datos de las 25 parcelas estudiadas. Recordamos que estamos pensando en escribir el código necesario para automatizar en la medida de lo posible la búsqueda del mejor modelo de producción, de tal forma que cuando el sistema contemple un mayor número de parcelas, la ejecución de los cuadernos nos siga generando el mejor modelo de producción posible.