import numpy as np
import pandas as pd

df = pd.DataFrame({'genero': np.repeat(np.array(['Mujeres', 'Hombres']), 150), 'deporte': np.repeat(np.array(
    ['Beisbol', 'Baloncesto', 'Tenis', 'Futbol', 'Beisbol', 'Baloncesto', 'Tenis', 'Futbol']), (34, 40, 58, 18, 34, 52, 20, 44))})

datos = pd.crosstab(index=df['genero'], columns=df['deporte'], margins=True)

print(datos)

print(datos.iloc[1, 3])

# Probabilidad de ser mujer dado que el individuo prefiera el beisbol

resultado = datos.iloc[1, 1]/datos.iloc[2, 1]

print(resultado)


# Probabilidad de preferir baloncesto dado que el individuo es hombre

resultado = datos.iloc[0, 0]/datos.iloc[2, 0]

print(resultado)

# Probabilidad de ser hombre dado que el individuo prefiere tenis

resultado = datos.iloc[0, 3]/datos.iloc[2, 3]

print(resultado)

# Probabilidad de preferir futbol dado que es mujer

resultado = datos.iloc[2, 1]/datos.iloc[2, 2]
