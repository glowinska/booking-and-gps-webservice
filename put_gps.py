import http.client
import json
from base64 import b64encode
import datetime

conn = http.client.HTTPConnection('localhost:5000')
userAndPass = b64encode(b"grawer:tajnePRZEZpoufne").decode("ascii")
headers = {'Content-type': 'application/json', 'Authorization' : 'Basic %s' %  userAndPass}

json_body = {'id' : 'lastgps', 'tid': '5', 'date' : '2020-10-15 08:22:57', 'co' : "52°8'45,6''N+21°0'50,0''E" }
json_data = json.dumps(json_body)

conn.request('PUT', '/lastgps', json_data, headers)

response = conn.getresponse()
print(response.read().decode())


