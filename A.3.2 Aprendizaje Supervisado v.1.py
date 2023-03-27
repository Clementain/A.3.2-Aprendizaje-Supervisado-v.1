import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB

sintomas = [[1, 1, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 1, 0], [
    1, 1, 1, 1], [0, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 0, 1, 1]]

diagnostico = ["Infección de garganta", "Alergia", "Resfriado", "Alergia",
               "Infección de garganta", "Resfriado", "Resfriado", "Infección de garganta", "Resfriado"]

df = pd.DataFrame(sintomas, columns=[
                  'Fiebre', 'Dolor de garganta', 'Congestión', 'Dolor de cabeza'])
df['Diagnóstico'] = diagnostico

# Crear un objeto de modelo Naive Bayes
modelo_NB = GaussianNB()

# Entrenar el modelo con los datos de síntomas y diagnósticos
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
modelo_NB.fit(X, y)


print("Escriba 1 para Si y 0 para No")
a = int(input("El paciente sufre de Fiebre: "))
b = int(input("El paciente sufre de Dolor de garganta: "))
c = int(input("El paciente sufre de Congestión: "))
d = int(input("El paciente sufre de Dolor de cabeza: "))

# Definir una combinación de síntomas
sintomas_nuevos = [[a, b, c, d]]

# Predecir la probabilidad de cada enfermedad para la combinación de síntomas dada
probabilidades = modelo_NB.predict_proba(sintomas_nuevos)

# Mostrar las probabilidades para cada enfermedad
diagnosticos = modelo_NB.classes_
for i, diagnostico in enumerate(diagnosticos):
    probabilidad = probabilidades[0, i]
    print(f"La probabilidad de tener {diagnostico} es {probabilidad}")
