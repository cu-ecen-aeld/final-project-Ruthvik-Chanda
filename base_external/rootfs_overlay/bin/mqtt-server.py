#Filename: Server-Subscriber.py
#Auther: Ruthvik R Chanda
#Description: This python script works as mqtt server-subscriber
#Reference: https://github.com/eclipse/paho.mqtt.python
#         : https://github.com/cu-ecen-aeld/buildroot-assignments-base/wiki/MQTT-Python-Example
#         : https://github.com/cu-ecen-aeld/buildroot-assignments-base/tree/9648e6530170935479d6e8cd86a845a177529c0f/base_external/rootfs_overlay/bin/MQTT

#Importing Modules
try:
	import paho
	import paho.mqtt.client as mqtt

#Error checking for module import
except Exception as e:
	print(e)

#port is the network port of the server host to connect to.
Port=1883
# Maximum period in seconds between communications with the broker.
Keepalive=60
try:
	# This is the Subscriber
	print("Air Quality Monitoring Server")

	#Function Defination: https://github.com/eclipse/paho.mqtt.python/blob/1eec03edf39128e461e6729694cf5d7c1959e5e4/src/paho/mqtt/subscribe.py#L26
	def on_connect(client, userdata, flags, rc):
	  print("Connected with result code "+str(rc))
	  client.subscribe("topic/test")

	#Function Defination: https://github.com/eclipse/paho.mqtt.python/blob/4f53d64675e4d1e9c78ce9fb2e450ba717dad3da/examples/client_sub.py#L28  
	def on_message(client, userdata, msg):
	  recieved_payload=msg.payload.decode()
	  print("'%s'" %recieved_payload)	
	  if recieved_payload == "Sending test data to Server...":
	    print("Success! Test data has been received at server from client side")
	
    # Client Constructor
	# Function Defination: https://github.com/eclipse/paho.mqtt.python#client-1
	client = mqtt.Client()

	#Connect to a remote broker.
	#Function defination:https://github.com/eclipse/paho.mqtt.python/blob/1eec03edf39128e461e6729694cf5d7c1959e5e4/src/paho/mqtt/client.py#L908
	client.connect("localhost",Port,Keepalive)

	client.on_connect = on_connect
	client.on_message = on_message

	client.loop_forever()
	
#Error Checking for script.
except Exception as e:
	print(e)
