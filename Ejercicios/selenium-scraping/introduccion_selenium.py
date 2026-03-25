# ==========================================================
# SELENIUM CON BOOKS TO SCRAPE
# ==========================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os


def iniciar_navegador():
    options = Options()

    # Ejecutar Chrome sin abrir ventana
    options.add_argument("--headless=new")

    # Tamaño de ventana virtual para que la web cargue en modo escritorio
    options.add_argument("--window-size=1920,1080")

    # En Windows puede ayudar cuando usamos headless
    options.add_argument("--disable-gpu")

    # Reduce ruido en consola
    options.add_argument("--log-level=3")

    # 👇 CAMBIO CLAVE: webdriver-manager gestiona el driver automáticamente
    servicio = Service(ChromeDriverManager().install())

    # Crear y devolver el navegador con esas opciones
    driver = webdriver.Chrome(service=servicio, options=options)
    return driver

# ----------------------------------------------------------
# 1. CREAR CARPETA PARA GUARDAR LAS CAPTURAS
# ----------------------------------------------------------

carpeta_capturas = "capturas_libros"

if not os.path.exists(carpeta_capturas):
    os.makedirs(carpeta_capturas)

# ----------------------------------------------------------
# 2. CREAR EL NAVEGADOR
# ----------------------------------------------------------

driver = iniciar_navegador()

# ----------------------------------------------------------
# 3. ABRIR LA WEB
# ----------------------------------------------------------

# driver.get("https://books.toscrape.com/")

# # Captura inicial
# driver.save_screenshot(f"{carpeta_capturas}/01_inicio.png")

# print("TÍTULO DE LA PÁGINA:")
# print(driver.title)
# print("-------------------------------------")

# ----------------------------------------------------------
# 4. COMPROBAR EL ENCABEZADO PRINCIPAL
# ----------------------------------------------------------

# titulo_principal = driver.find_element(By.TAG_NAME, "h1")

# print("ENCABEZADO PRINCIPAL:")
# print(titulo_principal.text)
# print("-------------------------------------")

# ----------------------------------------------------------
# 5. SACAR LOS LIBROS DE LA PRIMERA PÁGINA
# ----------------------------------------------------------

# libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

# print("NÚMERO DE LIBROS EN LA PRIMERA PÁGINA:")
# print(len(libros))
# print("-------------------------------------")

# print("DATOS DE LOS LIBROS DE LA PRIMERA PÁGINA:")

# for libro in libros:
#      titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
#      precio = libro.find_element(By.CLASS_NAME, "price_color").text
#      disponibilidad = libro.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()

#      print("Título:", titulo)
#      print("Precio:", precio)
#      print("Disponibilidad:", disponibilidad)
#      print("-----------------------")

# ----------------------------------------------------------
# 6. ENTRAR EN EL PRIMER LIBRO
# ----------------------------------------------------------

# primer_libro = driver.find_element(By.CSS_SELECTOR, "article.product_pod h3 a")
# titulo_antes = primer_libro.get_attribute("title")

# print("VAMOS A ENTRAR EN ESTE LIBRO:")
# print(titulo_antes)
# print("-------------------------------------")

# primer_libro.click()

# # Captura dentro del detalle del libro
# driver.save_screenshot(f"{carpeta_capturas}/02_detalle_libro.png")

# titulo_detalle = driver.find_element(By.TAG_NAME, "h1").text
# precio_detalle = driver.find_element(By.CLASS_NAME, "price_color").text
# disponibilidad_detalle = driver.find_element(By.CLASS_NAME, "instock").text.strip()

# print("DATOS DEL LIBRO EN SU FICHA:")
# print("Título:", titulo_detalle)
# print("Precio:", precio_detalle)
# print("Disponibilidad:", disponibilidad_detalle)
# print("-------------------------------------")

# ----------------------------------------------------------
# 7. VOLVER ATRÁS
# ----------------------------------------------------------

# driver.back()

# # Captura tras volver a la portada
# driver.save_screenshot(f"{carpeta_capturas}/03_vuelta_portada.png")

# print("HEMOS VUELTO A LA PÁGINA PRINCIPAL")
# print(driver.title)
# print("-------------------------------------")

# ----------------------------------------------------------
# 8. SACAR TODAS LAS CATEGORÍAS
# ----------------------------------------------------------

# categorias = driver.find_elements(By.CSS_SELECTOR, "div.side_categories ul li ul li a")

# print("CATEGORÍAS DISPONIBLES:")

# for categoria in categorias:
#     print(categoria.text.strip())

# print("-------------------------------------")

# ----------------------------------------------------------
# 9. ENTRAR EN LA CATEGORÍA TRAVEL
# ----------------------------------------------------------

# for categoria in categorias:
#      if categoria.text.strip() == "Travel":
#          categoria.click()
#          break

# # Captura dentro de la categoría Travel
# driver.save_screenshot(f"{carpeta_capturas}/04_categoria_travel.png")

# titulo_categoria = driver.find_element(By.TAG_NAME, "h1").text

# print("HEMOS ENTRADO EN LA CATEGORÍA:")
# print(titulo_categoria)
# print("-------------------------------------")

# print("LIBROS DE LA CATEGORÍA TRAVEL:")

# libros_travel = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

# for libro in libros_travel:
#      titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
#      precio = libro.find_element(By.CLASS_NAME, "price_color").text

#      print("Título:", titulo)
#      print("Precio:", precio)
#      print("-----------------------")

# ----------------------------------------------------------
# 10. VOLVER A LA PORTADA
# ----------------------------------------------------------

# driver.back()

# Captura al volver a la portada
# driver.save_screenshot(f"{carpeta_capturas}/05_portada_otra_vez.png")

# ----------------------------------------------------------
# 11. PASAR A LA SIGUIENTE PÁGINA
# ----------------------------------------------------------

# siguiente = driver.find_element(By.CSS_SELECTOR, "li.next a")
# siguiente.click()

# Captura de la segunda página
# driver.save_screenshot(f"{carpeta_capturas}/06_segunda_pagina.png")

# print("HEMOS PASADO A LA SIGUIENTE PÁGINA")
# print("URL actual:", driver.current_url)
# print("-------------------------------------")

# print("LIBROS DE LA SEGUNDA PÁGINA:")

# libros_pagina_2 = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

# for libro in libros_pagina_2:
#      titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
#      precio = libro.find_element(By.CLASS_NAME, "price_color").text

#      print("Título:", titulo)
#      print("Precio:", precio)
#      print("-----------------------")

# ----------------------------------------------------------
# 12. CERRAR NAVEGADOR
# ----------------------------------------------------------



# ==========================================================
# EJERCICIOS DE SELENIUM SOBRE BOOKS TO SCRAPE
# ==========================================================
#
# WEB DE TRABAJO:
# https://books.toscrape.com/
#
# IDEAS GENERALES:
# - Usa como base la práctica guiada que ya hemos visto.
# - Intenta reutilizar la función iniciar_navegador().
# - Si lo necesitas, guarda capturas para verificar en qué parte de la web estás.
#
# Estos ejercicios no son solo para “sacar datos”, sino para aprender a:
# - recorrer elementos
# - tomar decisiones
# - navegar por la web
# - comparar resultados
# - guardar información
# ==========================================================


# ==========================================================
# EJERCICIO 1
# MOSTRAR TODAS LAS CATEGORÍAS DISPONIBLES
# ==========================================================
#
# Mostrar todas las categorías que aparecen en la barra lateral.
# ==========================================================

driver.get("https://books.toscrape.com/")

categorias = driver.find_elements(By.CSS_SELECTOR, "div.side_categories ul li ul li a")

print("\n\nCATEGORÍAS DISPONIBLES:")
for index, categoria in enumerate(categorias):
    if index != 0:
        print(end=", ")
    print(categoria.text.strip(), end="")
print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 2
# COMPROBAR QUE EL TÍTULO COINCIDE AL ENTRAR EN UN LIBRO
# ==========================================================
#
# Entrar en un libro de la portada y comprobar si el título visible en la
# portada coincide con el título de la ficha del libro.
# ==========================================================

primer_libro = driver.find_element(By.CSS_SELECTOR, "article.product_pod h3 a")
titulo_portada = primer_libro.get_attribute("title")

primer_libro.click()

titulo_detalle = driver.find_element(By.TAG_NAME, "h1").text

if titulo_portada == titulo_detalle:
    print(f"El título '{titulo_detalle}' coincide tanto en la portada como en el detalle")
else:
    print(f"Los títulos no coinciden:\n{titulo_portada} en la portada y '{titulo_detalle}' en el detalle")

driver.back()

print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 3
# LIBRO MÁS CARO DE LA PRIMERA PÁGINA
# ==========================================================
#
# Recorre todos los libros de la primera página y muestra:
# - el título del libro más caro
# - su precio
# ==========================================================

libros_primera_pagina = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

mayor_precio = 0
titulo_mayor_precio = ""
for libro in libros_primera_pagina:
    titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
    precio = float(libro.find_element(By.CLASS_NAME, "price_color").text.replace("£", ""))
    if precio > mayor_precio:
        mayor_precio = precio
        titulo_mayor_precio = titulo

print(f"El libro con mayor precio (£{mayor_precio}) es {titulo_mayor_precio}")

print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 4
# CONTAR CUÁNTOS LIBROS CUESTAN MÁS DE 50 LIBRAS
# ==========================================================
#
# Es recomendable crear una lista para el ejercicio 5.
#
# Mostrar:
# - cuántos libros de la primera página cuestan más de 50 libras
# - qué títulos son
# ==========================================================

contador = 0
for libro in libros_primera_pagina:
    precio = float(libro.find_element(By.CLASS_NAME, "price_color").text.replace("£", ""))
    if precio > 50:
        contador = contador + 1

print(f"Hay un total de {contador} en la primera página que cuestan más de 50 libras")

print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 5
# ENTRAR EN EL PRIMER LIBRO QUE CUESTA MÁS DE 50 LIBRAS Y SACAR DATOS
# ==========================================================
#
# Obtener del primer libro que cuesta más de 50 libras:
# - título
# - precio
# - disponibilidad
# - categoría
# ==========================================================

for libro in libros_primera_pagina:
    precio = float(libro.find_element(By.CLASS_NAME, "price_color").text.replace("£", ""))
    if precio > 50:
        enlace_titulo = libro.find_element(By.CSS_SELECTOR, "h3 a")
        titulo = enlace_titulo.get_attribute("title")
        if libro.find_element(By.CLASS_NAME, "instock"):
            disponibilidad = ""
        else:
            disponibilidad = "no "
        categoria = ""
        
        enlace_titulo.click()

        breadcrumb = driver.find_elements(By.CSS_SELECTOR, "ul.breadcrumb li")
        if breadcrumb:
            categoria = breadcrumb[2].text

        print(f"El primer libro que cuesta más de £50 es \"{titulo}\" ({precio})", end="")
        print(f", se encuentra {disponibilidad}disponible y pertenece a la categoría es {categoria}")

        driver.back()
        
        break

print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 6
# ENTRAR EN LA CATEGORÍA Humor Y ANALIZARLA
# ==========================================================
#
# Entrar en la categoría Humor y mostrar:
# - el nombre de la categoría
# - cuántos libros aparecen en esa página
# - cuál es el libro más caro de esa categoría
# ==========================================================

for categoria in categorias:
    nombre_categoria = categoria.text.split()[0]
    if nombre_categoria == "Humor":
        categoria.click()
        libro_mas_caro = ""
        precio_libro = 0
        cantidad_categoria = driver.find_element(By.CSS_SELECTOR, "form.form-horizontal strong").text
        libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        for libro in libros:
            precio = float(libro.find_element(By.CSS_SELECTOR, "p.price_color").text.replace("£", ""))
            if precio > precio_libro:
                precio_libro = precio
                libro_mas_caro = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
                
        print(f"La categoría {nombre_categoria} tiene {cantidad_categoria} libros y el más caro es \"{libro_mas_caro}\"")
        driver.back()
        break

print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 7
# AVERIGUAR EL PRECIO MEDIO DE UNA CATEGORÍA
# ==========================================================
#
# Entra en una categoría, por ejemplo Childrens, y calcula:
# - cuántos libros tiene esa categoría
# - el precio medio de esos libros
# ==========================================================

for categoria in categorias:
    nombre_categoria = categoria.text.split()[0]
    if nombre_categoria == "Childrens":
        categoria.click()
        precio_libros = 0
        cantidad_categoria = int(driver.find_element(By.CSS_SELECTOR, "form.form-horizontal strong").text)
        siguiente_pagina = driver.find_element(By.CSS_SELECTOR, "li.next a")
        numero_paginas = 0
        while siguiente_pagina:
            numero_paginas = numero_paginas + 1
            libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
            for libro in libros:
                precio = float(libro.find_element(By.CSS_SELECTOR, "p.price_color").text.replace("£", ""))
                precio_libros = precio_libros + precio
            try:
                siguiente_pagina = driver.find_element(By.CSS_SELECTOR, "li.next a")
                siguiente_pagina.click()
            except:
                break
                
        precio_medio = round((precio_libros / cantidad_categoria), 2)
        print(f"La categoría {nombre_categoria} tiene {cantidad_categoria} libros y el precio medio es £{precio_medio}")

        for index in range(numero_paginas):
            driver.back()

        break

print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 8
# RECORRER 3 PÁGINAS Y ENCONTRAR EL LIBRO MÁS CARO
# ==========================================================
#
# Recorrer las 3 primeras páginas y averiguar:
# - cuál es el libro más caro
# - cuánto cuesta
# - en qué página estaba
# ==========================================================

precio_mas_caro = 0
libro_mas_caro = ""
pagina_mas_caro = 0
for index in range(3):
    libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    for libro in libros:
        precio = float(libro.find_element(By.CSS_SELECTOR, "p.price_color").text.replace("£", ""))
        if precio > precio_libro:
            precio_mas_caro = precio
            libro_mas_caro = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            pagina_mas_caro = index + 1
    
    siguiente_pagina = driver.find_element(By.CSS_SELECTOR, "li.next a")
    siguiente_pagina.click()

print(f"El libro más caro de las tres primeras páginas es \"{libro_mas_caro}\", cuesta £{precio_mas_caro} y está en la pagina {pagina_mas_caro}")

for _ in range(3):
    driver.back()

print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 9
# BUSCAR EL LIBRO MÁS BARATO Y EL MÁS CARO Y COMPARAR SUS ESTRELLAS
# ==========================================================
#
# Recorre las siete primeras páginas y guarda en una lista:
# - título
# - precio
# - estrellas
#
# Después muestra:
# - cuál es el libro más barato y cuántas estrellas tiene
# - cuál es el libro más caro y cuántas estrellas tiene
# - cuál de los dos tiene mejor valoración
# ==========================================================

def obtener_puntuacion(atributos):
    puntuacion = [atributo for atributo in atributos if atributo != "star-rating"]
    match puntuacion:
        case 'One':
            return 1
        case 'Two':
            return 2
        case 'Three':
            return 3
        case 'Four':
            return 4
        case 'Five':
            return 5
        case _:
            return 0

lista_libros = []

for index in range(7):
    libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    for libro in libros:
        star_rating = libro.find_element(By.CSS_SELECTOR, "p.star-rating")
        puntuacion = obtener_puntuacion(star_rating.get_attribute("class").split())
        precio = float(libro.find_element(By.CSS_SELECTOR, "p.price_color").text.replace("£", ""))
        titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        objeto_libro = {
            "titulo": titulo,
            "precio": precio,
            "puntuacion": puntuacion
        }
        lista_libros.append(objeto_libro)

    
    siguiente_pagina = driver.find_element(By.CSS_SELECTOR, "li.next a")
    siguiente_pagina.click()

lista_libros.sort(key=lambda libro: libro["precio"])

print(lista_libros[0])
print(lista_libros[-1])

for _ in range(7):
    driver.back()

driver.save_screenshot(f"{carpeta_capturas}/0{index}_inicio.png")

print("\n-------------------------------------\n")

# ==========================================================
# EJERCICIO 10
# COMPARAR DOS CATEGORÍAS
# ==========================================================
#
# Elige dos categorías, por ejemplo:
# - Humor
# - Mystery
#
# En cada una de ellas guarda en una lista:
# - título
# - precio
#
# Después compara:
# - cuántos libros aparecen en cada una
# - cuál tiene el libro más caro
# - cuál tiene el precio medio más alto
#
# IMPORTANTE:
# Si una categoría tiene varias páginas, debes tener en cuenta todos los libros
# de todas sus páginas, no solo los de la primera.
# ==========================================================


# ==========================================================
# EJERCICIO 11
# CONTAR CUÁNTOS LIBROS HAY EN CADA CATEGORÍA
# ==========================================================
#
# Recorre todas las categorías de la web y guarda en una lista:
# - nombre de la categoría
# - número de libros que contiene
#
# Después muestra:
# - cuántos libros tiene cada categoría
# - qué categoría es la que más libros tiene
#
# IMPORTANTE:
# Si una categoría tiene varias páginas, debes contar todos los libros
# de todas sus páginas, no solo los de la primera.
# ==========================================================


# ==========================================================
# EJERCICIO 12
# ENCONTRAR LOS LIBROS CON 5 ESTRELLAS Y ORDENARLOS POR PRECIO
# ==========================================================
#
# Recorre todas las páginas y guarda en una lista:
# - título
# - precio
# - estrellas
#
# Después quédate solo con los libros que tengan 5 estrellas y ordénalos
# de mayor a menor precio.
#
# Muestra el ranking resultante.
# ==========================================================


# ==========================================================
# EJERCICIO 13
# EL MEJOR LIBRO
# ==========================================================
#
# Recorre libros y guarda en una lista:
# - título
# - precio
# - estrellas
# - disponibilidad
#
# El objetivo es encontrar el primer libro que cumpla estas condiciones:
# - cuesta menos de 20 libras
# - tiene 5 estrellas
# - está disponible
#
# Después muestra todos sus datos.
# ==========================================================

driver.quit()

print("NAVEGADOR CERRADO")
print("LAS CAPTURAS SE HAN GUARDADO EN LA CARPETA:", carpeta_capturas)