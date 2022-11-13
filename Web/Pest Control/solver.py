#!/usr/bin/env python3
import paho.mqtt.client as mqtt
from base64 import b64decode
from PIL import Image
import io
from pytesseract import pytesseract
from tqdm import tqdm

messages = []
pbar = tqdm(total=100)

def on_connect(client, userdata, flags, rc):
    client.subscribe("#")
    pbar.update(0)

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    messages.append(msg.payload.decode())
    pbar.update(50*len(messages))
    if len(messages)==2:
        solve_ctf(messages)
        client.disconnect()

def solve_ctf(messages):
    messages.sort()
    messages = list(map(lambda x : x.split()[-1], messages))
    message = "".join(messages)
    image_bytes = b64decode(message.encode())
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    pbar.close()
    print(text.strip())
    
if __name__=="__main__":
    client = mqtt.Client()
    client.username_pw_set("ctf", "ctfftw")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("34.78.240.11", 1883, 60)
    client.loop_forever()
