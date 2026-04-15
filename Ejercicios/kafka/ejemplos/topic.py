from confluent_kafka.admin import AdminClient, NewTopic

admin_client = AdminClient({'bootstrap.servers': 'localhost:9092'})

nombre_topic = 'testtopic'
particiones = 3

nuevo_topic = NewTopic(
    topic=nombre_topic,
    num_partitions=particiones
)

resultado = admin_client.create_topics(new_topics=[nuevo_topic])

for topic, future in resultado.items():
    try:
        future.result()
        print(f"Se ha creado el topic {topic} con {particiones} particiones.")
    except Exception as e:
        print(f"No se pudo crear el topic {topic}. Error: {e}")