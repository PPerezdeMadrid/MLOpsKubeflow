import pandas as pd
import numpy as np

df = pd.read_csv('XXXXXXXXXXXXXXXXX')

# Añadimos una columna MES, Nota, Precio
df['Mes'] = np.random.choice(['Marzo', 'Abril', 'Mayo'], size=len(df))
df['NotaConsumidor'] = np.random.randint(0, 11, size=len(df))




