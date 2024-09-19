class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  
  def introduce(self):
    print(f'I am {self.name}. I am {self.age} years old and i am a {self.gender}')

me = Person('Stanley', 22, 'Male')   

me.introduce()