#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import json
import os

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    #print ("Connected with result code "+str(rc))
    client.subscribe('esp8266/arduino/s02', 0)

def on_message(client, userdata, msg):
    #print (msg.topic+" "+str(msg.payload))
    result = json.loads(msg.payload)
    #print result["PIRSTATUS"]
    if result["PIRSTATUS"] == 1:
       print ("Ouch")
       os.system('/usr/bin/pmset displaysleepnow &')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('192.168.10.10', 1883, 10)
client.loop_start()

try:
    while True:
        try:
            time.sleep(1)
    
        except Exception, e:
            print e.__doc__
            print e.message      
            sys.exit(1)

except KeyboardInterrupt:
    sys.exit(1)

