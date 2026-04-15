from confluent_kafka import Consumer

nombre_topic = 'testtopic'
grupo_consumers = 'testgrupo'

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': grupo_consumers,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([nombre_topic])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            print("No hay ningn mensaje. Sigo escuchando")
            continue
        print(f"Valor Mensaje: {msg.value().decode('utf-8')}")
        print(f"Clave: {msg.key()}")
        print(f"Particion: {msg.partition()}")
        print(f"Offset: {msg.offset()}")

except KeyboardInterrupt:
    pass

finally:
    consumer.close()