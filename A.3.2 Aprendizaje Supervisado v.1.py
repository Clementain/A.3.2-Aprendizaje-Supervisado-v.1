import pandas as pd
import numpy as np

# Crear dataframe con datos de enfermedades y síntomas
df = pd.DataFrame({
    'Enfermedad': ['Alergia', 'Alergia', 'Alergia', 'Alergia', 'Infección de garganta', 'Infección de garganta', 'Infección de garganta', 'Infección de garganta', 'Resfriado', 'Resfriado', 'Resfriado', 'Resfriado'],
    'Síntoma': ['Fiebre', 'Dolor de garganta', 'Congestión', 'Dolor de cabeza', 'Fiebre', 'Dolor de garganta', 'Congestión', 'Dolor de cabeza', 'Fiebre', 'Dolor de garganta', 'Congestión', 'Dolor de cabeza'],
    'Casos': [19, 17, 19, 16, 14, 11, 15, 12, 13, 20, 27, 16]
})

tabla_contingencia = pd.crosstab(
    df.Enfermedad, df.Síntoma, values=df.Casos, aggfunc='sum')
tabla_contingencia.loc['Total enfermedad'] = tabla_contingencia.sum()
tabla_contingencia['Total síntoma'] = tabla_contingencia.sum(axis=1)
print(tabla_contingencia)
