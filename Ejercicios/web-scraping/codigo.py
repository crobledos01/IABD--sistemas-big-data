from pathlib import Path
from bs4 import BeautifulSoup

path = "./Ejercicios/web-scraping/index.html"
page = Path(path).read_text(encoding="utf-8")
soup = BeautifulSoup(page, "html.parser")
try:
  # Nivel 1
  print("Nivel 1:\n")
  # 1. Extrae el texto del h1 usando find y usando select_one.
  h1_find = soup.find("h1").get_text(strip=True)
  print("h1 usando find:", h1_find)
  h1_select = soup.select_one("h1").get_text(strip=True)
  print("h1 usando select: ", h1_select)
  # 2. Extrae el texto del párrafo intro.
  intro = soup.select_one(".intro").get_text(strip=True)
  print("intro:", intro)
  # 3.Imprime todas las categorías mostrando codigo -> nombre.
  categorias = soup.find_all("li", class_="cat")
  print("Lista de categorías:")
  for cat in categorias:
      codigo = cat.get("data-cat")
      nombre = cat.get_text(strip=True)
      print(f"{codigo} -> {nombre}")
  # Nivel 2
  print("\nNivel 2:\n")
  # 4. Crea una lista solo con los códigos data-cat.
  codigos = [cat.get("data-cat") for cat in soup.select(".cat")]
  print("Lista de códigos data-cat: ", codigos)
  # 5. Crea un diccionario donde la clave sea codigo y el valor sea nombre.
  dicc_categorias = {}
  for li in soup.select(".cat"):
      codigo = li.get("data-cat")
      nombre = li.get_text(strip=True)
      dicc_categorias[codigo] = nombre
  print("Diccionario de categorías: ", dicc_categorias)
  # 6. Cuenta cuántas categorías hay.
  cuenta_categorias = len(soup.select(".cat"))
  print(f"Hay {cuenta_categorias} categorías")
  # Nivel 3
  print("\nNivel 3:\n")
  # 7. Extrae los productos en una lista de diccionarios con nombre, precio, stock.
  productos = []
  categorias = []
  filas_productos = soup.find_all("table")[0].find_all("tr")
  for tr in filas_productos:
      producto = {}
      td_list = tr.find_all("td")
      if not td_list:
          th_list = tr.find_all("th")
          for th in th_list:
              categorias.append(th.get_text(strip=True))
          continue
      for index, td in enumerate(td_list):
          producto[categorias[index].lower()] = td.get_text(strip=True)
      productos.append(producto)
  print("Lista de productos:")
  for producto in productos:
      print(producto)
  # 8. Crea una lista con los productos con stock == 0.
  prod_sin_stock = [prod for prod in productos if int(prod["stock"]) == 0]
  print("Productos sin stock:", prod_sin_stock)
  # 9. Calcula el valor total de inventario sumando precio * stock.
  valor_total = sum(float(prod["precio"]) * int(prod["stock"]) for prod in productos)
  print("Valor total del inventario:", valor_total)
  # Nivel 4
  print("\nNivel 4:\n")
  # 10. Modifica el HTML: cambia id="productos" por id="tabla_productos" y adapta tu selector (etiqueta o atributo que buscamos).
  # Se ha sustituido el id en el HTML por tabla_productos
  # 11. Añade una fila nueva a la tabla con un producto inventado.
  # <tr class="fila"><td>Servidor</td><td>899.99</td><td></td></tr>
  # 12. Modifica el HTML para que un dato sea incorrecto (por ejemplo, stock vacío o no numérico) y adapta tu código para que el programa no se detenga y siga funcionando.
  # El producto Servidor no tiene stock
except:
  print("Error")