import os
import pandas as pd

sheet = pd.read_csv('produtos.csv')
code_list = pd.to_numeric(sheet['Código'], errors='coerce') # Convertendo valores para numérico

for code in code_list:
    if pd.notna(code): # Verificando se código é NaN (Not a Number)
        name_folder = int(code)
        print(name_folder)
        directory = f"C:/Users/Monta Tudo/Documents/PRODUTOS/{name_folder}"
        os.mkdir(directory)
    else:
        print(f"{code} - Número inválido ou vazio!")