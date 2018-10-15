import requests
import json
header = {'Content-Type' : "application/json"}
body = json.dumps({'name' : 'ololo', 'position' : 'olololo'})
for id in [168, 169, 170, 171, 172, 173, 174, 175, 176, 177]:
response = requests.post('http://example.com/candidates', headers=header, data=body)
response.status_code
print(response.status_code)
print(response.json())