La vista minable que hemos obtenido representa los datos necesarios para crear un modelo de producción para el cultivo. El [próximo entregable](https://github.com/alesteba/tfg/tree/main/entregables) es el desarrollo de uno o varios cuadernos de jupyter con modelos de inteligencia artificial para la tabla anterior.

![](figures/view-capture.PNG)

En el punto en el que estamos, podemos pensar en las múltiples vistas que se pueden generar a partir de los datos persistidos en la BD. Desde aquí desarrollaremos la automatización de la búsqueda del mejor modelo posible para la vista anterior, pero siempre teniendo en cuenta que a partir de los datos almacenados podemos predecir muchos otros valores, no solo la producción de un cultivo. 

```python

X_train, X_test, y_train, y_test= train_test_split(
    
    X,y,
    train_size   = 0.8,
    random_state = SEED,
)
```


Resaltamos esta idea debido a que es el punto más fuerte del trabajo realizado. La arquitectura obtenida para la aplicación nos permite generar diferentes vistas con el objetivo de utilizar la información en diversos estudios. Los índices vegetativos y la información almacenada sobre de los cultivos se pueden presentar en el formato necesario que el estudio requiera. 

Por último, deberíamos poder utilizar este modelo obtenido dentro de la arquitectura de la aplicación para predecir,  cómo evolucionan los cultivos que se están monitorizando. El punto en el que se encuentra la arquitectura soporta casi de forma directa la inclusión de las predicciones de la aplicación.

```python

clf = RandomForestRegressor(**CV_rfr.best_params_)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(y_pred)

```

