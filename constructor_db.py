import pandas as pd
import numpy as np
import sqlite3

# Lectura del archivo
df = pd.read_csv("datos.csv")

# Se hace la limpieza, ya que hay datos que aparecen Nan
df = df.dropna(subset=["Source", "Plx", "Gmag", "BPmag", "RPmag"])

# Para evitar errores con el paralaje
df = df[df["Plx"] > 0]

# Color
df["color"] = df["BPmag"] - df["RPmag"]
df["mag_absoluta"] = df["Gmag"] + 5 * np.log10(df["Plx"]) - 10

# Conexion a una base de datos local
conn = sqlite3.connect("datos_mision.db")

df.to_sql("estrellas", conn, if_exists="replace", index=False)

conn.close()
print("La limpieza y migracion a datos_mision.db se ha hecho exitosamente")

