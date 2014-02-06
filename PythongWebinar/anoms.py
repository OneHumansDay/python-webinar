class AnonObject(dict):
    __getattr__ = dict.get
    __seattr__ = dict.__setitem__



person = {
          "name" : "Michael",
          "age": 40
          }

print(person)
print(person["name"]);
print(person.name);