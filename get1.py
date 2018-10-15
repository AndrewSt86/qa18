A2333import requests
import json
for id in [168, 169, 170, 171, 172, 173, 174, 175, 176, 177]:
response = requests.get('http://example.com/candidates')
print(response.status_code)
print(response.json())