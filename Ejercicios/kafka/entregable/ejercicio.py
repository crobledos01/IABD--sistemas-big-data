import pandas as pd
from confluent_kafka import Producer, Consumer, TopicPartition
from confluent_kafka.admin import AdminClient, NewTopic
from io import StringIO

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

    nombre_topic = 'kafkapython'
    particion_ID = 0
    p = Producer(cliente)

    for index, row in df.iterrows():
        message = f"{row['empresa']}, {row['pais']}, {row['sector']},{row['precio_eur_LY']}, {row['precio_eur_CY']}, {row['empleados']}, {row['ingresos_millones']}, {row['ingresos_millones']}, {row['crecimiento_pct']},"
        p.produce(topic=nombre_topic, value=message, partition=particion_ID)
    p.flush()

except Exception as e:
    print(f"Error al crear el topic: {e}")
    exit()

print("\nEl csv se ha enviado correctamente al topic 'kafkapython' en la partición 0.")

print("\n--------\n")

# Ejercicio 3

print("\nEjercicio 3: Recepción de datos\n")

nombre_topic = 'kafkapython'
grupo_consumers = 'testgrupo'
particion_ID = 0

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': grupo_consumers, 'auto.offset.reset': 'earliest'})
c.assign([TopicPartition(nombre_topic, particion_ID)])

columnas_df = ['empresa', 'pais', 'sector','precio_eur_LY', 'precio_eur_CY', 'empleados', 'ingresos_millones', 'ingresos_millones', 'crecimiento_pct']
df_reconstruido = pd.DataFrame(columns=columnas_df)
try:
    while df.shape[0] > df_reconstruido.shape[0]:
        msg = c.poll(1.0)
        if msg is None:
            print("No hay ningún mensaje")
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue

        # Añadimos el mensaje a la lista de mensajes
        message_data = StringIO(msg.value().decode('utf-8'))
        row_data = pd.read_csv(message_data, header=None, names=columnas_df)
        
        df_reconstruido = pd.concat([df_reconstruido, row_data], ignore_index=True)

except Exception as e:
    print(f"Error en la lectura de los datos: {e}")
    exit()
finally:
    c.close()
    
print("\nDataFrame reconstruido:")
print(df_reconstruido)

print("\n--------\n")

# Ejercicio 4
