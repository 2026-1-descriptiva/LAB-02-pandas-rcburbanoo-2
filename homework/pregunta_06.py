"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.tsv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    df=pd.read_csv("files/input/tbl1.tsv",sep="\t")
    return sorted(df["c4"].str.upper().unique()) #se selecciona la columna c4, se convierte a mayusculas con str.upper() y se obtienen los valores únicos con unique(), luego se ordenan alfabéticamente con sorted()

print(pregunta_06() )