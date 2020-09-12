import requests
import time
tv_ip = '192.168.1.44'
ambilight_power = "http://%s:1925/6/ambilight/power" % (tv_ip)
key_input = "http://%s:1925/6/input/key" % (tv_ip)

ambilight_power_status = requests.get(ambilight_power).json()['power']

while ambilight_power_status == 'On':
  requests.post(key_input, json={"key":"AmbilightOnOff"})
  ambilight_power_status = requests.get(ambilight_power).json()['power']
  time.sleep(0.1)
requests.post(key_input, json={"key":"Back"})
