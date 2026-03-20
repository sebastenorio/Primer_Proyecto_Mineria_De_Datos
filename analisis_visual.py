import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Conexión con el archivo creado previamente
conexion = sqlite3.connect('datos_mision.db')

# Se define la consulta SQL
consulta = "SELECT color, mag_absoluta FROM estrellas;"
# Pongo a Pandas a ejecutar la consulta, para convertir el resultado en un DataFrame
df = pd.read_sql_query(consulta, conexion)
# se cierra la conexion
conexion.close()

# Diagrama
plt.scatter(df["color"], df["mag_absoluta"], s=1)

plt.gca().invert_yaxis()

plt.xlabel("Color")
plt.ylabel("Magnitud Absoluta")
plt.title("Diagrama Hertzsprung-Russell")

plt.savefig("resultado.png", dpi=300)
plt.show()
