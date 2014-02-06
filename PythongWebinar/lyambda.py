class Person:
    def __init__(self, name, age, hobby):
        self.hobby = hobby
        self.age = age
        self.name = name

    def __repr__(self):
        return "{0} is {1} and likes {2}".format(self.name, self.age, self.hobby)

people = [
    Person("Jeff", 50, "Biking"),
    Person("Ann", 40, "Js"),
    Person("Tl", 20, "2ing"),
    Person("Lees", 10, "iking")
]

bikers = [
        
          p
          for p in people
          if p.hobby == "Biking"
            
        ]

bikers.sort(key = lambda p: p.Name);
print(bikers)