import pandas as pd
from confluent_kafka import Producer, Consumer, TopicPartition
from confluent_kafka.admin import AdminClient, NewTopic
from io import StringIO
import matplotlib.pyplot as plt

# Ejercicio 1

df = pd.DataFrame(pd.read_csv('data_empresas.csv'))

print("\nEjercicio 1: Cargar csv y mostrar número de filas, columnas y tipos de datos\n")

num_filas = df.shape[0]
num_columnas = df.shape[1]
tipo_datos = df.dtypes

print(f"El csv tiene {num_filas} filas y {num_columnas} columnas.")
print("Tipos de datos:")
print(tipo_datos)

print("\n--------\n")

# Ejercicio 2

print("\nEjercicio 2: Envío estructurado a Kafka\n")

cliente = {'bootstrap.servers': 'localhost:9092'}

admin_client = AdminClient(cliente)

# Se crea el topic con una partición

try:
    nombre_topic = 'kafkapython'
    particiones = 1
    nuevotopic = NewTopic(topic=nombre_topic, num_partitions=particiones)
    result = admin_client.create_topics(new_topics=[nuevotopic])

    particion_ID = 0
    p = Producer(cliente)

    for index, row in df.iterrows():
        message = f"{row['empresa']}, {row['pais']}, {row['sector']},{row['precio_eur_LY']}, {row['precio_eur_CY']}, {row['empleados']}, {row['ingresos_millones']}, {row['crecimiento_pct']}"
        p.produce(topic=nombre_topic, value=message, partition=particion_ID, key=row['empresa'])
    p.flush()

except Exception as e:
    print(f"Error al crear el topic: {e}")
    exit()

print("\nEl csv se ha enviado correctamente al topic 'kafkapython' en la partición 0.")

print("\n--------\n")

# Ejercicio 3

print("\nEjercicio 3: Recepción de datos\n")

grupo_consumers = 'testgrupo'
particion_ID = 0

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': grupo_consumers, 'auto.offset.reset': 'earliest'})
c.assign([TopicPartition(nombre_topic, particion_ID)])

columnas_df = ['empresa', 'pais', 'sector','precio_eur_LY', 'precio_eur_CY', 'empleados', 'ingresos_millones', 'crecimiento_pct']
df_reconstruido = pd.DataFrame(columns=columnas_df)
try:
    while df.shape[0] > df_reconstruido.shape[0]:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            continue

        # Añadimos el mensaje a la lista de mensajes
        message_data = StringIO(msg.value().decode('utf-8'))
        row_data = pd.read_csv(message_data, header=None, names=columnas_df)
        
        df_reconstruido = pd.concat([df_reconstruido, row_data], ignore_index=True)

        if msg.key() is not None:
            print(f"Clave del mensaje: {msg.key()}")

except Exception as e:
    print(f"Error en la lectura de los datos: {e}")
    exit()
finally:
    c.close()

# Convertir columnas numéricas a tipos numéricos
numeric_columns = ['precio_eur_LY', 'precio_eur_CY', 'empleados', 'ingresos_millones', 'crecimiento_pct']
for col in numeric_columns:
    df_reconstruido[col] = pd.to_numeric(df_reconstruido[col], errors='coerce')
    
print("\nDataFrame reconstruido:")
print(df_reconstruido)

print("\n--------\n")

# Ejercicio 4

print("\nEjercicio 4: Nueva información\n")

df_reconstruido['variacion'] = df_reconstruido['precio_eur_CY'] - df_reconstruido['precio_eur_LY']
print(df_reconstruido[['empresa', 'variacion']])

# Ejercicio 5

print("\nEjercicio 5: detección de anomalías\n")

crecimiento_negativo = df_reconstruido[df_reconstruido['crecimiento_pct'] < 0]
valores_sospechosos = df_reconstruido[df_reconstruido['ingresos_millones'] < 0]
print("\nEmpresas con crecimiento negativo:")
print(crecimiento_negativo[['empresa', 'crecimiento_pct']])

print("\nEmpresas con valores sospechosos:")
print(valores_sospechosos[['empresa', 'ingresos_millones']])

# Ejercicio 6

print("\nEjercicio 6: Uso de claves en Kafka\n")
print("Se ha añadido la clave tanto al p.produce del ejercicio 2 como a la recolección de mensajes del ejercicio 3")

# Ejercicio 7

print("\nEjercicio 7: Distribución por particiones\n")

try:
    nombre_topic = 'kafkaporparticiones'
    particiones = 3
    nuevotopic = NewTopic(topic=nombre_topic, num_partitions=particiones)
    result = admin_client.create_topics(new_topics=[nuevotopic])

    p = Producer(cliente)

    for index, row in df.iterrows():
        message = f"{row['empresa']}, {row['pais']}, {row['sector']},{row['precio_eur_LY']}, {row['precio_eur_CY']}, {row['empleados']}, {row['ingresos_millones']}, {row['crecimiento_pct']}"
        p.produce(topic=nombre_topic, value=message, key=row['empresa'])
    p.flush()

except Exception as e:
    print(f"Error al crear el topic: {e}")
    exit()

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': grupo_consumers, 'auto.offset.reset': 'earliest'})
c.assign([TopicPartition(nombre_topic, p) for p in range(particiones)])

# Se cuentan el número de mensajes en la partición 1 para el siguiente ejercicio
cuenta_particion_1 = 0

conteo = 0
try:
    while df.shape[0] > conteo:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            continue

        if msg.key() is not None:
            conteo += 1
            print(f"La empresa {msg.key()} ha sido añadida a la partición {msg.partition()}")
            if msg.partition() == 1:
                cuenta_particion_1 += 1

except Exception as e:
    print(f"Error en la lectura de los datos: {e}")
    exit()
finally:
    c.close()

# Ejercicio 8

print("\nEjercicio 8: Consumidor parcial\n")

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': grupo_consumers, 'auto.offset.reset': 'earliest'})
c.assign([TopicPartition(nombre_topic, 1, 0)])

# Parte del ejercicio 9
nombre_csv = 'datos_particion_1.csv'
columnas_df = ['empresa', 'pais', 'sector','precio_eur_LY', 'precio_eur_CY', 'empleados', 'ingresos_millones', 'crecimiento_pct']
df_particion_1 = pd.DataFrame(columns=columnas_df)

conteo = 0
try:
    while cuenta_particion_1 > conteo:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            continue

        if msg.key() is not None:
            conteo += 1
            print(f"La empresa {msg.key()} ha sido añadida a la partición {msg.partition()}")

            # Parte del ejercicio 9
            message_data = StringIO(msg.value().decode('utf-8'))
            row_data = pd.read_csv(message_data, header=None, names=columnas_df)
            df_particion_1 = pd.concat([df_particion_1, row_data], ignore_index=True)

except Exception as e:
    print(f"Error en la lectura de los datos: {e}")
    exit()
finally:
    c.close()

# Parte del ejercicio 9
if df_particion_1.empty:
    print("No se recibieron mensajes en la partición 1 para guardar en CSV.")
else:
    df_particion_1.to_csv(nombre_csv, index=False)
    print(df_particion_1.head())

# Ejercicio 9

print("\nEjercicio 9: Guardar datos de la partición 1 en CSV\n")

if not df_particion_1.empty:
    print(f"El CSV se ha generado correctamente con el nombre {nombre_csv}. 10 Primeras filas:")
    print(df_particion_1.head())

# Ejercicio 10

print("\nEjercicio 10: Análisis simple\n")

empresa_mayores_ingresos = df_reconstruido.loc[df_reconstruido['ingresos_millones'].idxmax()]
empresa_mayor_crecimiento = df_reconstruido.loc[df_reconstruido['crecimiento_pct'].idxmax()]

print(f"La empresa con mayores ingresos es {empresa_mayores_ingresos['empresa']} ({empresa_mayores_ingresos['ingresos_millones']}M€)")
print(f"La empresa con mayor crecimiento es {empresa_mayor_crecimiento['empresa']} ({empresa_mayor_crecimiento['crecimiento_pct']}%)")

# Ejercicio 11

print("\nEjercicio 11: Visualización comparativa\n")

empresas_top_ingresos = df_reconstruido.nlargest(5, 'ingresos_millones')

plt.figure(figsize=(10, 6))
plt.bar(empresas_top_ingresos['empresa'], empresas_top_ingresos['precio_eur_LY'], alpha=0.6, label='Precio LY')
plt.bar(empresas_top_ingresos['empresa'], empresas_top_ingresos['precio_eur_CY'], alpha=0.6, label='Precio CY')

plt.xlabel('Empresa')
plt.ylabel('Precio en EUR')
plt.title('Comparación de precios')

plt.show()