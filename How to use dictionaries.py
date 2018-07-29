# Dictionaries in Python
d = {}
# Or d = dict()
# d = {"George": 24, "Tom": 32}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16
print(d["George"])
print(d["Tom"])
print(d["Jenny"])
d["Jenny"] = 20
print(d["Jenny"])
# Keys are commonly strings or numbers
d[10] = 100
print(d[10])
# How to iterate over key-value pairs
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")
