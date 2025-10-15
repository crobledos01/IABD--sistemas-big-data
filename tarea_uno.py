import pandas as pd

# Cargamos el dataset desde una URL pública
url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# BLOQUE 1
# 1. Explica qué información contiene el dataset, cuántas filas y columnas tiene, y qué representa cada una.

print("Información del dataset:")
print(netflix.info())
print("Filas x columnas: ", netflix.shape)

# 2. Calcula cuántos títulos hay de cada tipo (por ejemplo, películas o series) e interpreta el resultado.

print("Tipos de contenido:")
print(netflix.groupby("type")["title"].count())

# 3. Muestra las diez producciones más recientes junto con su país y año de estreno.

print("Producciones más recientes:")
print(netflix[["title", "release_year", "production_countries"]].sort_values("release_year", ascending=False).head(10))

# 4. Indica cuál es la producción más antigua registrada y comenta si el dato parece coherente.

print(netflix[["release_year", "title"]].sort_values("release_year", ascending=True).head(1))
# Se publicó en 1945, así que parece tener sentido

# 5. Muestra las producciones estrenadas en el año 2020 y cuenta cuántas hay.
# 6. Muestra todas las producciones dirigidas por Steven Spielberg (si aparece en el dataset).
# 7. Crea un nuevo DataFrame con los títulos que contengan la palabra Love o Amor.
# 8. Calcula qué porcentaje del total del catálogo corresponde a producciones de Estados Unidos.
# 9. Muestra las cinco producciones con mayor duración e interpreta el resultado.
# 10. Identifica los cinco países con más títulos producidos y ordénalos de mayor a menor.
# 11. Indica qué año tiene más estrenos y cuántos títulos se publicaron en ese periodo.
# 12. Representa mediante un gráfico la evolución del número de títulos a lo largo de los años.
# 13. Crea un gráfico de barras con los diez países que más títulos han producido.
# 14. Añade una nueva columna llamada “década” que agrupe los años de estreno (por ejemplo, 1990, 2000, 2010...)
# y analiza qué década concentra más estrenos.
# 15. Crea una visualización que compare el número de películas y series por año.
# 16. Busca todas las producciones de género terror o horror y analiza cuál es la más reciente y de qué país procede.
# 17. Calcula cuántas producciones fueron realizadas en más de un país.
# 18. Indica qué director aparece con mayor frecuencia en el conjunto de datos.
# 19. Analiza cuáles son los géneros más comunes y en qué tipo de producción predominan.