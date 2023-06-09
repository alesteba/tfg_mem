Tras conseguir los datos con la forma correspondiente, exponemos los modelos de inteligencia artificial que vamos a utilizar para buscar el mejor modelo de producción de cultivo (kg) posible.

El problema que estamos buscando resolver es un problema de regresión, en el que conocemos la variable objetivo por el estudio de campañas anteriores. Los clientes, en este caso agricultores, quieren poder predecir cuántos kg de cultivo van a poder cosechar al final de la temporada (septiembre), o en estados previos de maduración (enero).

Los cuadernos que conforman el entregable contienen código que busca el mejor modelo posible para los datos importados con los índices y sus estadísticos. Los índices vegetativos registrados en diferentes fechas, junto con la variable de producción de campañas anteriores, tienen que poder predecir con precisión la campaña actual.

```python
# drop columns with negative mean.

for col in df.columns:

	df2 = df[col].mean()
	
	if (df2 < 0):
	
		df = df.drop(columns=[col], axis =1)
```

Antes de ejecutar código para los modelos, analizamos las relaciones entre las columnas y hacemos estudios de correlación y análisis de componentes principales, para ver si algunos datos de fechas que han llegado a este punto no añaden valor a la información que queremos predecir. Recordemos que puede que lleguen índices provenientes de imágenes tomadas entre nubes y entonces la información empeora el modelo.

Un análisis de componentes principales y la observación de las mejores columnas son el siguiente paso a la limpieza de columnas que se ha realizado en el preprocesamiento.

```python

rfe = RFE(estimator=DecisionTreeRegressor(), n_features_to_select=5)  
model = DecisionTreeRegressor()
pipeline = Pipeline(steps=[('s',rfe),('m',model)])

cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
n_scores = cross_val_score(pipeline, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)

print('MAE: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

```

Para la variable objetivo de producción también hacemos un pequeño análisis. Queremos ver si esta contiene outilers, para ello analizamos la distribución y seleccionamos aquellos valores que se alejan mucho de la media y desviación típica de la muestra. Es importante que los datos con los que vamos a predecir estén limpios para que el modelo obtenga una buena métrica, como puede ser el "mean absolute error", MAE, puntuación para problemas de regresión en el que el resultado está contemplado en las unidades de la variable analizada.

Una vez hemos analizado los datos y hemos limpiado los valores erróneos de los índices, procedemos a probar aquellos modelos de inteligencia artificial que mejor puedan predecir este valor de kg de producción. Los modelos que probamos son los siguientes.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MODEL</th>
      <th>PARAMS</th>
      <th>MAE</th>
      <th>MSE</th>
      <th>RMSE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>RandomForest</td>
      <td>{'rf__max_depth': 7, 'rf__max_features': 'sqrt', 'rf__n_estimators': 5, 'rf__random_state': 42}</td>
      <td>2282.013333</td>
      <td>1.464411e+07</td>
      <td>3826.762121</td>
    </tr>
    <tr>
      <th>0</th>
      <td>ElasticNet</td>
      <td>{'en__alpha': 10, 'en__l1_ratio': 0.7000000000000001, 'en__max_iter': 5}</td>
      <td>4668.784757</td>
      <td>4.217480e+07</td>
      <td>6494.212821</td>
    </tr>
    <tr>
      <th>4</th>
      <td>KNeighbors</td>
      <td>{'knn__metric': 'manhattan', 'knn__n_neighbors': 11, 'knn__weights': 'uniform'}</td>
      <td>5109.534545</td>
      <td>4.310770e+07</td>
      <td>6565.645200</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MLP</td>
      <td>{'mlpr__activation': 'tanh', 'mlpr__alpha': 0.05, 'mlpr__hidden_layer_sizes': (100, 50, 30), 'mlpr__learning_rate': 'adaptive', 'mlpr__max_iter': 50, 'mlpr__solver': 'sgd'}</td>
      <td>4599.475956</td>
      <td>4.323998e+07</td>
      <td>6575.711553</td>
    </tr>
    <tr>
      <th>1</th>
      <td>SVR</td>
      <td>{'svr__C': 5.0, 'svr__gamma': 0.01, 'svr__kernel': 'linear'}</td>
      <td>4129.801479</td>
      <td>4.749271e+07</td>
      <td>6891.495313</td>
    </tr>
  </tbody>
</table>

La tabla anterior muestra ciertas métricas para los algoritmos probados. Al ordenar la tabla por el RMSE vemos qué algoritmo predice un poco mejor y observamos aquellos hiperparámetros que mejor score obtienen.

```python
df_sorted = df.sort_values(by='RMSE', ascending=True, na_position='first');
```

```python
best_models = []

for index, row in df_sorted.iterrows():

	model_str, model_prm= row["MODEL"], row["PARAMS"]
	model_type = getattr(sys.modules[__name__], model_str)
	rm_pre_parms = rm_dict_pre(model_prm) # modify dict keys
	best_model = model_type(**rm_pre_parms)
	best_models.append(best_model)
```

```python
best_estimators = []

for idx, est in enumerate(best_models):

	best_estimators.append((est.__class__.__name__, est))
```

Como cada modelo aporta un punto de vista diferente, vamos a utilizar los resultados obtenidos para generar un modelo ensemble que generalice las predicciones de los anteriores. Utilizaremos las métricas obtenidas para establecer el orden en el que construir un modelo 'stacking'. Como estimador final nos quedamos como el mejor modelo obtenido al ordenar la tabla anterior por el valor del RMSE obtenido para cada uno de ellos, es decir, el RandomForestRegressor.

```python
reg = StackingRegressor(
		estimators=estimators,
		final_estimator=estimators[0][1])

reg.fit(x, y)

y_pred_e = reg.predict(x)
```

A continuación mostramos una gráfica para cada modelo en la que vemos la relación entre los valores actuales y los valores predichos por el modelo. Esta pequeña visualización nos permite ver si cada algoritmo sobreajusta a los datos de entrenamiento o realmente tiene el rango que necesitamos. El punto más interesante es el análisis del modelo 'stacking' en el que vemos que es capaz de inferir los estilos de los algoritmos anteriores.

![Comparación de los algoritmos. Valores reales vs. los predichos por cada uno de los modelos utilizados.](figures/models-predictions.png)

Hemos analizado cada algoritmo con la intención de ver si modeliza correctamente nuestro problema de regresión, pero no es nuestro objetivo final que el modelo prediga con exactitud: solo queremos dejar automatizada una pequeña visualización de las relaciones entre los índices para así poder intuir qué modelo nos puede funcionar mejor. De hecho, los datos representativos con los que trabajamos nos impiden buscar un modelo real preciso.
