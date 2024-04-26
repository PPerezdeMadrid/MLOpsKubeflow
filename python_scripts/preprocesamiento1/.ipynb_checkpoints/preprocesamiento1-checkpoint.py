
def preprocesamiento1(df):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler, LabelEncoder

    # Escalar caracteristicas
    scaler = StandardScaler()
    # df_mid = df.drop('Quality', axis=1).scale().as_data_frame()
    scaler.fit(df.drop('Quality', axis=1))
    scaled_features = scaler.transform(df.drop('Quality', axis=1))
    df_transformado = pd.DataFrame(scaled_features, columns=df.columns[:-1])

    # Codificamos la variable Quality a (1 y 0)
    label_encoder = LabelEncoder()
    df_transformado['Quality_encoded'] = label_encoder.fit_transform(df['Quality'])

    # Eliminar valores NA
    df_transformado.drop('Quality', axis=1)

    # Eliminar valores atipicas
     # Calcular el rango intercuartílico (IQR)
    df_numerico = df_transformado.drop(columns=['Quality'])
    df_numerico = df_numerico.select_dtypes(include=['number'])
    q1 = df_numerico.quantile(0.25)
    q3 = df_numerico.quantile(0.75)
    iqr = q3 - q1

    # Definir los límites inferior y superior para identificar valores atípicos
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    # Eliminar los valores atípicos
    df_transformado = df_numerico[~((df_numerico < lower_limit) | (df_numerico > upper_limit)).any(axis=1)]
    return df_transformado