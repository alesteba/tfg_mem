``` python

from core.models import *

import pandas as pd

# indices:
indices = ['ndvi', 'ndre']

def statistic_indices(indices = ['ndvi', 'ndre'], func=np.mean):

    df = pd.DataFrame()
    # para cada indice:

    for ind in indices:

        indice_p = Indice.objects.get(nombre=ind)

        for fecha in fechas:

            col_data = []

            # por cada iteración de esto tienes una fila en el df:
            for p in Parcela.objects.all():
                # la media de todos sus índices

                p_indices = Pixel.objects.filter(parcela=p)
                list_values = []

                for p_itr in p_indices:

                    qs =  Mirar_Indice.objects.get(
                    
                        pixel = p_itr,
                        indice = indice_p,
                        fecha = fecha # fecha para la columna:
                    )

                    import math
                    
                    # mirarmos que no sea nulo, porque se uede dar el caso
                    if ( not math.isnan(qs.valor) ):

                        list_values.append(qs.valor)

                # estadistico

                res = func(list_values)
                col_data.append(res)

            df[func.__name__ + '_' + ind +'_' +str(fecha)] = col_data

    return df
```

Con esta función que acabamos de definir podemos concatenar diferentes estadísticos de varios índices. Por el análisis realizado por el equipo, esta construcción no va a permitir acercarnos a un buen modelo de producción.

```python

df1 = statistic_indices(['ndvi', 'ndre'], np.mean)

df2 = statistic_indices(['ndvi', 'ndre'], np.sum)

df3 = pd.concat([df1, df2], axis=1)

df3

```

Vemos cómo creamos un data-frame con dos índices y dos estadísticos.