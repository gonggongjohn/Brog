import json

for x in json.loads(json.dumps({
    "a": [1, 2, 3],
    "b": "asdf"
}))["a"]:
    print(x)
