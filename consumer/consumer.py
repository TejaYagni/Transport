from kafka import KafkaConsumer
consumer = KafkaConsumer('transportation')
for msg in consumer:
	print(msg)
