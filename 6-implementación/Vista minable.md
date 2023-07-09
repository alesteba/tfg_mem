Hasta este punto habíamos insertado en la base da datos la información que provenía de diferentes fuentes. Hemos dotado de consistencia y relación a los datos y se ha creado un sistema con capacidad para hacer consultas sobre estos de forma ordenada y sencilla.

Ahora, fuera de la estructura de comandos de *Django* y utilizando el entorno virtual creado y los cuadernos integrados en la aplicación, escribimos el algoritmo para extraer los datos y dar la forma necesaria para los siguientes pasos.

El código que mostramos en este apartado corresponde con la generación de la vista tabulada con la que vamos a crear el modelo de producción de cultivo. Ahora realizamos el proceso inverso a la persistencia de datos que hemos realizado hasta este punto. Utilizamos la información y sus relaciones perisitidas en la base de datos de nuestro sistema para generar la vista minable que necesita el modelo predictivo. 

```python 

def statistic_indices(indices = ['ndvi', 'ndre'], func=np.mean):

    df = pd.DataFrame()
    
    col_ids = []
    
    for p in Parcela.objects.all():
    
        col_ids.append(p.idx)
        
    df['IDX'] = col_ids
    
    for ind in indices:

        indice_p = Indice.objects.get(nombre=ind)
        
        for fecha in fechas: 
        
            col_data = []
            
            # por cada iteración creamos una fila en el df:
            
            for p in Parcela.objects.all():
            
                # la media de todos sus índices
                
                p_indices = Pixel.objects.filter(parcela=p)
                
                list_values = []
                
                for p_itr in p_indices:
                
                    qs =  Mirar_Indice.objects.get(
                    
						pixel = p_itr, 
                        indice = indice_p, 
                        fecha = fecha # fecha para la columna:
                    )
                    
                    import math
                    
                    if ( not math.isnan(qs.valor) ):
                    
                        list_values.append(qs.valor)
                        
                # estadistico:añadir columna
                
                res = func(list_values)
                
                col_data.append(res)
                
            df[func.__name__ + '_' + ind +'_' +str(fecha)] = col_data
            
    return df
```

## Selección de features

El diseño de la vista minable es complicado; para ello trabajo con el equipo seleccionando los campos de la BD más importantes que formarán la tabla.  Nos centramos principalmente en los índices vegetativos registrados en diferentes fechas. 

Para poder predecir la producción de cultivo, incluimos en la vista varios estadísticos, como la media y el sumatorio para cada índice en cuatro fechas representativas de la evolución de este. El diseño de esta estructura proviene de un estudio previo realizado por el equipo en el que se ha concluido que ciertos estadísticos en unas fechas calibradas funcionan bien para predecir la producción. 

Hablábamos anteriormente de entornos virtuales, por el momento la aplicación utiliza un solo entorno virtual Python, pero este punto del trabajo podría hacer uso de un entorno separado con las librerías de ciencia de datos instaladas, de tal forma que separaríamos dos procesos importantes. Hay que destacar que en el trabajo me estoy encargando del proceso para hacer pruebas, pero serán diferentes miembros del equipo los que usen estas tecnologías: para que podamos seguir escalando a medida que evolucione la aplicación, estos miembros tienen que poder utilizar los entornos creados.

## Variable Objetivo

Junto con los datos extraídos añadiremos la variable objetivo, "producción". Esta variable, aún sin almacenar en el modelo relacional, hace referencia a los kilos de producción de cada parcela en su cosecha, se obtiene a partir de históricos de campañas anteriores. A partir de ella, junto con las features anteriores, vamos a poder predecir la evolución del cultivo con precisión en estados concretos de su maduración. Se explica con detalle en el siguiente punto.

