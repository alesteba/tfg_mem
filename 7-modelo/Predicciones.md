Nuestro último paso en el pipeline mostrado anteriormente es la capacidad para utilizar el modelo y predecir qué cantidad de kg se pueden cosechar cuando se pasa una nueva parcela al sistema. A continuación mostramos cómo el último 'stage' del pipeline utiliza el modelo que acabamos de entenar para predecir sobre la vista minable.

```python

filename = 'script/finalized_model.sav'

df_x = pd.read_csv('script/view.csv')

loaded_model = pickle.load(open(filename, 'rb'))

y_pred_e = loaded_model.predict(df_x)

print(y_pred_e)

```

En este punto, deberíamos poder utilizar este modelo obtenido dentro de la arquitectura de la aplicación para predecir, cómo evolucionan los cultivos que se están monitorizando. El punto en el que se encuentra la arquitectura soporta casi de forma directa la inclusión de las predicciones de la aplicación.

![Predicción de la cantidad de Kg de cultivo que se va a cosechar. Resultado tras la ejecución del último 'stage' en el pipeline.](figures/predict.png)