import pandas as pd
import numpy as np

df = pd.read_csv('XXXXXXXXXXXXXXXXX')

# Añadimos una columna Nota, Precio
df['NotaConsumidor'] = np.random.randint(0, 11, size=len(df))
df['Temporada'] = np.random.randint(0, 2, size=len(df))
df['Estacion'] = np.random.choice(['Primavera', 'Verano', 'Otoño', 'Invierno'], size=len(df))




