import numpy as np
import pandas as pd

df = pd.DataFrame({'enfermedad': np.repeat(np.array(['Alergia', 'Infección de garganta', 'Resfriado']), (36, 27, 38)),
                   'sintomas': np.repeat(np.array(['Fiebre', 'DolorGarganta', 'Congestion', 'DolorCabeza']),
                                         (46, 48, 61, 44))})

datos = pd.crosstab(index=df['enfermedad'],
                    columns=df['sintomas'], margins=True)

print(df)
