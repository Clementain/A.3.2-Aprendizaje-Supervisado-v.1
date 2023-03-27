import numpy as np
import pandas as pd

sintomas = [[1, 1, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 1, 0], [
    1, 1, 1, 1], [0, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 0, 1, 1]]

diagnostico = ["Infección de garganta", "Alergia", "Resfriado", "Alergia",
               "Infección de garganta", "Resfriado", "Resfriado", "Infección de garganta", "Resfriado"]

df = pd.DataFrame(sintomas, columns=[
                  'Fiebre', 'Dolor de garganta', 'Congestión', 'Dolor de cabeza'])
df['Diagnóstico'] = diagnostico

df_melt = pd.melt(df, id_vars=['Diagnóstico'],
                  var_name='Síntoma', value_name='Valor')
datos = pd.crosstab(index=df_melt['Diagnóstico'], columns=[
                    df_melt['Síntoma'], df_melt['Valor']], margins=True, margins_name='Total')

print(datos)
