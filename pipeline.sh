echo "Descarga de datos"

wget -O datos.csv "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query=SELECT+TOP+50000+Source,Plx,Gmag,BPmag,RPmag+FROM+%22I/355/gaiadr3%22+WHERE+Plx%3E5"

echo "Bases de datos"
python3 constructor_db.py

echo "Análisis y visualización de la gráfica"
python3 analisis_visual.py

echo "Todo se ha hecho correctamente"
