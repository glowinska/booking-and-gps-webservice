import http.client
import json
from base64 import b64encode
import datetime

conn = http.client.HTTPConnection('localhost:5000')
userAndPass = b64encode(b"grawer:tajnePRZEZpoufne").decode("ascii")
headers = {'Content-type': 'application/json', 'Authorization' : 'Basic %s' %  userAndPass}


json_body = {'id' : 'lastbooking', 'tid': '4', 'cid' : '123', 'cc' : 'FD00000000', 'ow' : '123', 'cr' : '123456', 'fk' : 'Button1', 'date' : '2020-10-15 08:00:00', 'valid' : '', 'gpsco' : "52°8'45,6''N+21°0'50,0''E" ,'addInfo' : 'TEST', 'base64jpg' : 'fotobased64jpg'}
json_data = json.dumps(json_body)

conn.request('PUT', '/lastbooking', json_data, headers)

response = conn.getresponse()
print(response.read().decode())


