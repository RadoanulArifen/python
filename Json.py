

#conversiton of Json onbject int o their  respective Python object that means Deserialization.

import json

data = {
    'Name' : "Arifen",
    'Age': 20,
    'Is_logged _in' : True,
    'test' : None,
}

#serialization (python to Json)
Json_string = json.dumps(data,indent=4)
print(Json_string)
print(type(Json_string))

#deserialization (Json to Python)
data = '{"Name" : "Arifen", "Age": 20,"Is_logged _in" : true}'
python_dict = json.loads(data)
print(python_dict, type(python_dict))