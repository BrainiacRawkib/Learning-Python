import json

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)

print(rec)

x = json.dumps(rec)

print(x)

i = json.loads(x)

print(i)

print(i == rec)

json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)

print(open('testjson.txt').read())

p = json.load(open('testjson.txt'))

print(p)





