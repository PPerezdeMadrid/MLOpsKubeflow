import numpy as np
from typing import NamedTuple
import kfp
#from kfp import dsl, components as comp
from kfp import components
from kfp.v2.dsl import component

@component(
    #base_image="python:3.11",
    packages_to_install=['numpy'],
)
def preprocesamiento2(df):
    # Añadimos una columna Nota, Temporada, Estacion
    df['NotaConsumidor'] = np.random.randint(0, 11, size=len(df))
    df['Temporada'] = np.random.randint(0, 2, size=len(df))
    df['Estacion'] = np.random.choice(['Primavera', 'Verano', 'Otoño', 'Invierno'], size=len(df))
    return df

# preprocesamiento2_component = comp.func_to_container_op(preprocesamiento2, packages_to_install=['numpy'])