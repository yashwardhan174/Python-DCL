#serealization

import json
with open("filehandling/sample.json","w+") as f:
    d = {1:"Alice",2:"Ben"}
    json_str = json.dumps(d)
    f.write(json_str)


#deserializxation

with open("filehandling/sample.json","w+") as f:
    d = {1:"Alice",2:"Ben"}
    json.dump(d,f)
    # f.write(json_str)
    f.seek(0)
    pobject = json.load(f)
    print(pobject , type(pobject))