import pandas as pd
import random as rd

def generar_datos_df(dataframe, cantidad_filas): 
    columnas = list(dataframe.columns) 
    nueva_cosecha = pd.DataFrame()

    for i in range(len(columnas)):
        valor_min = dataframe[columnas[i]].min()
        valor_max = dataframe[columnas[i]].max()
        if columnas[i] == 'Quality':
            nueva_cosecha[columnas[i]] = [rd.choice(['Good', 'Bad']) for _ in range(cantidad_filas)] 
        else:
            nueva_cosecha[columnas[i]] = [rd.uniform(valor_min, valor_max) for _ in range(cantidad_filas)]
            
    nueva_cosecha['Mes'] = [rd.randint(1, 12) for _ in range(cantidad_filas)]
    return nueva_cosecha