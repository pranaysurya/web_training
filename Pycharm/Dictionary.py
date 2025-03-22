x = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "date": 1964,
    "list": [1, 2, 3, 4, 5]
}

print (x)

print (x["brand"])

print (x.keys())

print (x.values())


x["color"] = "red"

x["date"] = "2025"

print (x.pop("date"))
x.popitem()
print (x)

x.clear()

print (x)
