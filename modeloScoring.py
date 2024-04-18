import h2o

from h2o.estimators import H2OXGBoostEstimator
from h2o.grid.grid_search import H2OGridSearch
from h2o.estimators import H2ODeepLearningEstimator
from h2o.estimators.random_forest import H2ORandomForestEstimator

h2o.init()

"""
Argumentos
@df : nombre del dataframe
@mes: mes de los datos
"""
df = ''
mes = ""

data = h2o.H2OFrame(df)  

#creacion de subconjuntos
# Size	Weight	Sweetness	Softness	HarvestTime	Ripeness	Acidity	Quality_encoded	Size_HarvestTime
predictors = ["Precio", "NotaConsumidor", "Size", "Weight", "Sweetness", "Softness", "HarvestTime", "Ripeness", "Acidity"]#, "Size_HarvestTime"] #<- Ya no está Size_harvesttime
response = "Quality_encoded"

data[response] = data[response].asfactor() #datos marzo --> factor

# Dividir los datos en train + dev + test
train, test, dev = data.split_frame(ratios=[0.75, 0.15], destination_frames = ['train_df', 'test_df', 'val_df'],
                                    seed=566)

#Entrenamos el modelo
xgb = H2OXGBoostEstimator()
xgb.train(x=predictors, y=response, training_frame=train, validation_frame=dev)

#Pasamos a scoring con las predicciones del modelo, hacemos una predicción y evaluarla
#predecir:
pred = xgb.predict(test)

#evaluación: 
evaluacion = xgb.model_performance(test)

#Creamos los archivos de predicción y scoring
pred = pred.as_data_frame()

#ahora lo guardamos en un .csv
pred.to_csv("predicciones_marzo.csv", index=False)

with open("scoring_"+str(mes)+".txt", "w") as file:
    file.write(str(evaluacion))