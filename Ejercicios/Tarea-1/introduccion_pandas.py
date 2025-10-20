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
print("1. Información del dataset:")
print(netflix.info())
print("Filas x columnas: ", netflix.shape)

# 2. Calcula cuántos títulos hay de cada tipo (por ejemplo, películas o series) e interpreta el resultado.

print()
print()
print("2. Tipos de contenido:")
print(netflix.groupby("type")["title"].count())

# 3. Muestra las diez producciones más recientes junto con su país y año de estreno.

print()
print()
print("3. Producciones más recientes:")
print(netflix[["title", "release_year", "production_countries"]].sort_values("release_year", ascending=False).head(10))

# 4. Indica cuál es la producción más antigua registrada y comenta si el dato parece coherente.

print()
print()
print("4. Película más antigua registrada:")
print(netflix[["release_year", "title"]].sort_values("release_year", ascending=True).head(1))
print("Se publicó en 1945, parece tener sentido ya que la primera emisión de una película se realizó en 1895")

# 5. Muestra las producciones estrenadas en el año 2020 y cuenta cuántas hay.

print()
print()
print(f"5. Número de películas estrenadas en 2020: {(netflix["release_year"] == 2020).sum()}")

# 6. Muestra todas las producciones dirigidas por Steven Spielberg (si aparece en el dataset). --> NO hay directores
# 7. Crea un nuevo DataFrame con los títulos que contengan la palabra Love o Amor.

print()
print()
titulos_amor_love = netflix[netflix["title"].str.contains("love|amor", case=False, na=False)]

# 8. Calcula qué porcentaje del total del catálogo corresponde a producciones de Estados Unidos.

print()
print()
num_prod_usa = netflix[netflix["production_countries"].str.contains("US", na=False)]
print(f"8. El número de producciones realizadas en EEUU es de {len(num_prod_usa)}, lo que implica un {round((len(num_prod_usa) / len(netflix) * 100), 2)}% sobre el total.")

# 9. Muestra las cinco producciones con mayor duración e interpreta el resultado.

print()
print()
print(netflix[["title", "type", "description", "release_year", "runtime"]].sort_values(by="runtime", ascending=False).head(5))
print("9. En este top solamente aparecen películas con duraciones excepcionales, predominando las décadas de los 70 y los 80")

# 10. Identifica los cinco países con más títulos producidos y ordénalos de mayor a menor.

print()
print()
paises = netflix["production_countries"].str.strip("[]").str.replace(" ", "").str.replace("'", "").dropna().str.split(",")
counter_paises = Counter(paises.sum())
cantidad_por_pais = pd.DataFrame(counter_paises.items(), columns=["country", "quantity"])
print("10. Países con más producciones:")
print(cantidad_por_pais.sort_values(by="quantity", ascending=False).head(5))

# 11. Indica qué año tiene más estrenos y cuántos títulos se publicaron en ese periodo.

print()
print()
cantidad_estrenos = netflix["release_year"].value_counts()
print(f"11. El año con más estrenos fue {cantidad_estrenos.idxmax()} con {cantidad_estrenos.max()} títulos.")

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
print(f"14. La década con más estrenos fue la de {estrenos_por_decada.idxmax()} con un total de {estrenos_por_decada.max()}")

# 15. Crea una visualización que compare el número de películas y series por año.

conteo_por_año = netflix.groupby(['release_year', 'type']).size().unstack(fill_value=0)
conteo_por_año.plot(kind="bar", figsize=(10, 5))
plt.title('Número de películas y series por año en Netflix')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Cantidad')
plt.show()

# 16. Busca todas las producciones de género terror o horror y analiza cuál es la más reciente y de qué país procede.

print()
print()
peliculas_de_terror = netflix[netflix["genres"].str.contains("terror|horror", case=False, na=False)]
print("16. Película de terror más reciente:")
print(peliculas_de_terror[["title", "release_year", "production_countries"]].sort_values("release_year", ascending=False).head(1))

# 17. Calcula cuántas producciones fueron realizadas en más de un país.

print()
print()
print(f"17. Producciones desarrolladas en más de un país: {len(netflix[netflix["production_countries"].str.contains(",", na=False)])}")

# 18. Indica qué director aparece con mayor frecuencia en el conjunto de datos. --> NO hay directores

# 19. Analiza cuáles son los géneros más comunes y en qué tipo de producción predominan.

print()
print()
generos = netflix["genres"].str.strip("[]").str.replace(" ", "").str.replace("'", "").dropna().str.split(",")
counter_generos = Counter(generos.sum())
cantidad_por_genero = pd.DataFrame(counter_generos.items(), columns=["genres", "quantity"])
total_cinco_mayores_generos = cantidad_por_genero.sort_values(by="quantity", ascending=False).head(5)

peliculas = netflix[netflix["type"] == "MOVIE"]
peliculas_por_genero = peliculas["genres"].str.strip("[]").str.replace(" ", "").str.replace("'", "").dropna().str.split(",")
counter_generos_peliculas = Counter(peliculas_por_genero.sum())
cantidad_peliculas_por_genero = pd.DataFrame(counter_generos_peliculas.items(), columns=["genres", "quantity"])

peliculas_cinco_mayores_generos = cantidad_peliculas_por_genero[cantidad_peliculas_por_genero["genres"].isin(total_cinco_mayores_generos["genres"])]
peliculas_cinco_mayores_generos = peliculas_cinco_mayores_generos.rename(columns={"quantity": "movies"})

cinco_mayores_generos = pd.merge(total_cinco_mayores_generos, peliculas_cinco_mayores_generos, on="genres")
cinco_mayores_generos["shows"] = cinco_mayores_generos["quantity"] - cinco_mayores_generos["movies"]

print("19. Estos son los cinco géneros más comunes:")
for index, fila in cinco_mayores_generos.iterrows():
    genero = fila["genres"]
    total = fila["quantity"]
    peliculas = fila["movies"]
    series = fila["shows"]
    comparacion = "más" if peliculas > series else "menos"

    print(f"{index + 1}: El género {genero}, que contiene {total} producciones con {peliculas} peliculas y {series} series. Por lo tanto, hay {comparacion} películas que series")
    
# 20. Encuentra el título con más caracteres y el título con menos caracteres.

print()
print()
netflix["title_length"] = netflix["title"].str.len()

titulo_mas_largo = netflix.loc[netflix["title_length"].idxmax()]
titulo_mas_corto = netflix.loc[netflix["title_length"].idxmin()]

print("20. Títulos según longitud de caracteres:")
print(f"Título más largo ({titulo_mas_largo['title_length']} caracteres): {titulo_mas_largo['title']}")
print(f"Título más corto ({titulo_mas_corto['title_length']} caracteres): {titulo_mas_corto['title']}")

# 21. Verifica si existen títulos repetidos

print()
print()
titulos_duplicados = netflix[netflix.duplicated(subset=["title"], keep=False)]
cantidad_duplicados = titulos_duplicados["title"].nunique()

print(f"21. Existen {cantidad_duplicados} títulos diferentes que están repetidos en el dataset.")
print("Ejemplos de títulos repetidos:")
print(titulos_duplicados["title"].value_counts())

# 22. ¿Qué país produce más comedias y dramas?

print()
print()

# Filtramos por comedias

comedias = netflix[netflix["genres"].str.contains("comedy", case=False, na=False)]

# Filtramos por dramas

dramas = netflix[netflix["genres"].str.contains("drama", case=False, na=False)]

# Función para contar países

def contar_paises(df):
    paises = df["production_countries"].dropna().str.strip("[]").str.replace(" ", "").str.replace("'", "").str.split(",")
    contador = Counter(paises.sum())
    return pd.DataFrame(contador.items(), columns=["country", "quantity"]).sort_values(by="quantity", ascending=False)

# Países con más comedias

paises_comedias = contar_paises(comedias)
pais_top_comedia = paises_comedias.iloc[0]

# Países con más dramas

paises_dramas = contar_paises(dramas)
pais_top_drama = paises_dramas.iloc[0]

print(f"22. País con más comedias: {pais_top_comedia['country']} con {pais_top_comedia['quantity']} títulos.")
print(f"País con más dramas: {pais_top_drama['country']} con {pais_top_drama['quantity']} títulos.")
