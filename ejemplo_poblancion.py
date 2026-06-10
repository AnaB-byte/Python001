import pandas as pd  

# Variables con los ficheros a importar
fichero_csv = "36680.csv"

# Nombres de los ficheros a escribir
escribir_csv = '36680.csv'

# Lee los datos de los ficheros
# Para la codificación estándar europea también se puede utilizar latin_1
leer_csv = pd.read_csv(fichero_csv,sep=';', encoding="utf-8")

# Imprime los primeros 10 
#print(leer_csv.head(10))
#print(leer_csv.head(10))

# Escribe en los ficheros (en el .csv solamente los 10 primeros registros)
with open(escribir_csv, 'w', encoding='utf-8') as write_csv:
    # index=False no muestra el índice
    write_csv.write(leer_csv.head(10).to_csv(sep=';', index=False))


    