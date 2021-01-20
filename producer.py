from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers='localhost:9092')
while(True):
    msg = 'some data in bytes ' + str(time.time())
    producer.send('poc-topic', bytes(msg, 'utf-8'))
    print("Message sent %s" , msg)
    time.sleep(1)
