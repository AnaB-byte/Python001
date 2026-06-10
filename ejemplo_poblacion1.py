import os
import shutil
import pandas as pd

# Ruta del CSV original
csv_origen = "36680.csv"

# Crear directorio si no existe
directorio_destino = "backup_csv"
os.makedirs(directorio_destino, exist_ok=True)

# Leer el CSV con pandas
df = pd.read_csv(csv_origen)

# Guardar una copia dentro del nuevo directorio
csv_copia = os.path.join(directorio_destino, "datos.csv")
df.to_csv(csv_copia, index=False)

print(f"Copia guardada en: {csv_copia}")