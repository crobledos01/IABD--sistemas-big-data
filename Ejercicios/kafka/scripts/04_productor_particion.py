from confluent_kafka import Producer

nombre_topic = 'pruebatopic'
mensaje = 'mensaje particion'
particion_ID = 0

p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce(topic=nombre_topic, value=mensaje, partition=particion_ID)
p.flush()