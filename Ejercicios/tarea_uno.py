import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Cargamos el dataset desde una URL pública
url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# BLOQUE 1
# 1. Explica qué información contiene el dataset, cuántas filas y columnas tiene, y qué representa cada una.

print()
print()
print("Información del dataset:")
print(netflix.info())
print("Filas x columnas: ", netflix.shape)

# 2. Calcula cuántos títulos hay de cada tipo (por ejemplo, películas o series) e interpreta el resultado.

print()
print()
print("Tipos de contenido:")
print(netflix.groupby("type")["title"].count())

# 3. Muestra las diez producciones más recientes junto con su país y año de estreno.

print()
print()
print("Producciones más recientes:")
print(netflix[["title", "release_year", "production_countries"]].sort_values("release_year", ascending=False).head(10))

# 4. Indica cuál es la producción más antigua registrada y comenta si el dato parece coherente.

print()
print()
print(netflix[["release_year", "title"]].sort_values("release_year", ascending=True).head(1))
print("Se publicó en 1945, parece tener sentido ya que la primera emisión de una película se realizó en 1895")

# 5. Muestra las producciones estrenadas en el año 2020 y cuenta cuántas hay.

print()
print()
print(f"Número de películas estrenadas en 2020: {(netflix["release_year"] == 2020).sum()}")

# 6. Muestra todas las producciones dirigidas por Steven Spielberg (si aparece en el dataset). --> NO hay directores
# 7. Crea un nuevo DataFrame con los títulos que contengan la palabra Love o Amor.

print()
print()
titulos_amor_love = netflix[netflix["title"].str.contains("love|amor", case=False, na=False)]

# 8. Calcula qué porcentaje del total del catálogo corresponde a producciones de Estados Unidos.

print()
print()
num_prod_usa = netflix[netflix["production_countries"].str.contains("US", na=False)]
print(f"El número de producciones realizadas en EEUU es de {len(num_prod_usa)}, lo que implica un {round((len(num_prod_usa) / len(netflix) * 100), 2)}% sobre el total.")

# 9. Muestra las cinco producciones con mayor duración e interpreta el resultado.

print()
print()
print(netflix[["title", "type", "description", "release_year", "runtime"]].sort_values(by="runtime", ascending=False).head(5))
print("En este top solamente aparecen películas con duraciones excepcionales, predominando las décadas de los 70 y los 80")

# 10. Identifica los cinco países con más títulos producidos y ordénalos de mayor a menor.

print()
print()
paises = netflix["production_countries"].str.strip("[]").str.replace(" ", "").str.replace("'", "").dropna().str.split(",")
counter_paises = Counter(paises.sum())
cantidad_por_pais = pd.DataFrame(counter_paises.items(), columns=["country", "quantity"])
print("Países con más producciones:")
print(cantidad_por_pais.sort_values(by="quantity", ascending=False).head(5))

# 11. Indica qué año tiene más estrenos y cuántos títulos se publicaron en ese periodo.

print()
print()
cantidad_estrenos = netflix["release_year"].value_counts()
print(f"El año con más estrenos fue {cantidad_estrenos.idxmax()} con {cantidad_estrenos.max()} títulos.")

# 12. Representa mediante un gráfico la evolución del número de títulos a lo largo de los años.

netflix["release_year"].value_counts().sort_index(ascending=True).plot(kind="bar", figsize=(10, 5))
plt.title("Número de películas publicadas por año")
plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.show()

# 13. Crea un gráfico de barras con los diez países que más títulos han producido.

#utilizando "cantidad_por_pais", creado en el ejercicio 10, podemos sacar una tabla con la estructura pais y cantidad de la que sacar la información
cantidad_ordenada = cantidad_por_pais.sort_values(by="quantity", ascending=False)
plt.figure(figsize=(10, 5))
plt.bar(cantidad_ordenada["country"].head(), cantidad_ordenada["quantity"].head())
plt.title("Paises con más producciones")
plt.xlabel("País")
plt.ylabel("Cantidad")
plt.show()

# 14. Añade una nueva columna llamada “década” que agrupe los años de estreno (por ejemplo, 1990, 2000, 2010...)
# y analiza qué década concentra más estrenos.

print()
print()
netflix["decada"] = (netflix["release_year"] // 10) * 10
estrenos_por_decada = netflix["decada"].value_counts().sort_index()
print(f"La década con más estrenos fue la de {estrenos_por_decada.idxmax()} con un total de {estrenos_por_decada.max()}")

# 15. Crea una visualización que compare el número de películas y series por año.
# 16. Busca todas las producciones de género terror o horror y analiza cuál es la más reciente y de qué país procede.
# 17. Calcula cuántas producciones fueron realizadas en más de un país.
# 18. Indica qué director aparece con mayor frecuencia en el conjunto de datos.
# 19. Analiza cuáles son los géneros más comunes y en qué tipo de producción predominan.