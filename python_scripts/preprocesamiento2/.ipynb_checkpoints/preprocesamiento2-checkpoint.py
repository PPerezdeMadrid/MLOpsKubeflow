def preprocesamiento2(df):
    import numpy as np
    # Añadimos una columna Nota, Temporada, Estacion
    df['NotaConsumidor'] = np.random.randint(0, 11, size=len(df))
    df['Temporada'] = np.random.randint(0, 2, size=len(df))
    df['Estacion'] = np.random.choice(['Primavera', 'Verano', 'Otoño', 'Invierno'], size=len(df))
    return df




