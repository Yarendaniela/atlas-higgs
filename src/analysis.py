import os
import pandas as pd

# Ruta absoluta del archivo
file_path = r"C:\Users\Yaren Daniela\Desktop\atlas-higgs\data\atlas-higgs-challenge-2014-v2.csv"

# Verificar si existe
print("Archivo existe:", os.path.exists(file_path))  # debe imprimir True

# Cargar CSV
df = pd.read_csv(file_path)
print("Datos cargados correctamente\n")

# Primeras filas
print(df.head())

# Información general
print(df.info())

# Estadísticas básicas
print(df.describe())