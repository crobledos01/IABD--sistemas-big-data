from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

producer.produce('testtopic', 'hola esto es una prueba')
producer.flush()