class Person:
    'this is person class'
    age = 10
    
    def greet(self):
        print('hello')
        
print(Person.age)
print(Person.greet)
print(Person.__doc__)