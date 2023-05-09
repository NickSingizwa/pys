import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(message.payload.decode())

topic = "chat"

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost")
client.subscribe(topic)

client.loop_forever()