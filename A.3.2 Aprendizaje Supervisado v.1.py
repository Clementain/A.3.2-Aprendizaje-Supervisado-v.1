import pandas as pd
import numpy as np

probAlergia = 0.0
probInfeccion = 0.0
probResfriado = 0.0
congestion = 0
dolorCabeza = 0
dolroGarganta = 0
fiebre = 0

df = pd.DataFrame({
    'Enfermedad': np.repeat(['Alergia', 'Infección de garganta', 'Resfriado'], [4, 4, 4]),
    'Síntoma': np.tile(['Fiebre', 'Dolor de garganta', 'Congestión', 'Dolor de cabeza'], 3),
    'Casos': [19, 17, 19, 16, 14, 11, 15, 12, 13, 20, 27, 16]
})

tabla_contingencia = pd.crosstab(
    df.Enfermedad, df.Síntoma, values=df.Casos, aggfunc='sum', margins=True)
print(tabla_contingencia)


def evaluarSintomas(condicion):
    if condicion == "alergia":
        row = 0
    elif condicion == "infeccion":
        row = 1
    elif condicion == "resfriado":
        row = 2

    if congestion == 1:
        sintoma1 = tabla_contingencia.iloc[row,
                                           0] / tabla_contingencia.iloc[3, 0]
    else:
        sintoma1 = 0

    if dolorCabeza == 1:
        sintoma2 = tabla_contingencia.iloc[row,
                                           1] / tabla_contingencia.iloc[3, 1]
    else:
        sintoma2 = 0

    if dolroGarganta == 1:
        sintoma3 = tabla_contingencia.iloc[row,
                                           2] / tabla_contingencia.iloc[3, 2]
    else:
        sintoma3 = 0

    if fiebre == 1:
        sintoma4 = tabla_contingencia.iloc[row,
                                           3] / tabla_contingencia.iloc[3, 3]
    else:
        sintoma4 = 0

    if congestion+dolorCabeza+dolroGarganta+fiebre == 0:
        return 0
    else:
        return ((sintoma1 + sintoma2 + sintoma3 + sintoma4)/(congestion+dolorCabeza+dolroGarganta+fiebre))

    # return (sintoma1 + sintoma2 + sintoma3 + sintoma4) / tabla_contingencia.ioc[row, 4]


while True:
    print("<--------- BIENVENIDO AL CONSULTORIO --------->")
    print("\nPor favor indique si presenta algun sintoma '1' para indicar que SI y '0' para indicar que NO")

    congestion = int(input("¿Tienes Congestion? -> "))
    dolorCabeza = int(input("¿Tienes Dolor de Cabeza? -> "))
    dolroGarganta = int(input("¿Tienes Dolor de Garganta? -> "))
    fiebre = int(input("¿Tienes fiebre? -> "))
    print("\n")

    probAlergia = round(evaluarSintomas("alergia"), 4) * 100
    probInfeccion = round(evaluarSintomas("infeccion"), 4) * 100
    probResfriado = round(evaluarSintomas("resfriado"), 4) * 100

    print("USTED PUEDE TENER....")
    print(f"Alergia: {probAlergia}%")
    print(f"Infeccion de garganta: {probInfeccion}%")
    print(f"Resfriado: {probResfriado}%")
