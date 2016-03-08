import json
print dir(json)
render = open("../web/templates/vmdata.txt",'r').readlines()
data = ''.join(i.strip("\n") for i in render)
json_data = json.dumps(data)
print json_data