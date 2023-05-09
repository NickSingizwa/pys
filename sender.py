import paho.mqtt.publish as publish

topic = "chat"

while True:
    message = input("Enter message: ")
    publish.single(topic, message, hostname="localhost")