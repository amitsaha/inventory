import requests
import sys
import json

with open('/proc/cpuinfo') as f:
    cpuinfo = f.read()

payload = {'mac': '11:22:33:44:55', 
           'cpuinfo': cpuinfo,
           }
r = requests.post(sys.argv[1], 
                  headers={'Content-Type': 'application/json'},
                  data=json.dumps(payload))
print r.text
