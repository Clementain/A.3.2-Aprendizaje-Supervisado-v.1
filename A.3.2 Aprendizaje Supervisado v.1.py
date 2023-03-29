import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Enfermedad': np.repeat(['Alergia', 'Infección de garganta', 'Resfriado'], [4, 4, 4]),
    'Síntoma': np.tile(['Fiebre', 'Dolor de garganta', 'Congestión', 'Dolor de cabeza'], 3),
    'Casos': [19, 17, 19, 16, 14, 11, 15, 12, 13, 20, 27, 16]
})

tabla_contingencia = pd.crosstab(
    df.Enfermedad, df.Síntoma, values=df.Casos, aggfunc='sum', margins=True)
print(tabla_contingencia)
