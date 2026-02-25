import json
"""with open("practice4/json/example.json","r") as i:
    a=json.load(i)"""
'''
print(a["Name"])
print(a["Age"])
print(a["Phone"])
print(a["Media"]["Onlyfans"])

print(a.keys())

del a["Media"]["Onlyfans"]
print(a)'''

"""a["Region"]=["Almaty","Astana","Kyzylorda"]
print(json.dumps(a,indent=3))

with open("practice4/json/example.json","w") as i:
    a=json.dump(a,i,indent=8)
"""
"""data = [
    {"Age" : 20,"car" : "Mersedes",
     "language" : {
         "kazakh" : 20,
         "russian" :10
     }
    }
]
print(json.dumps(data,indent=5,separators=(".","="),sort_keys=True))"""
with open("practice4/json/example.json","r") as i:
    a=json.load(i) 
print(json.dumps(a,indent=3,sort_keys=True,separators=(" ","=")))


