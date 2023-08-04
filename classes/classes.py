class Doll:
    """A doll"""
    name = 'This doll'
    material = "plastic"
    humanoid = True

    def speak(self):
        print("hello!!!")
      
    def learn_new_language(self):
        print(f'{self.name} is learning Italian')
         
barbie = Doll()
barbie.name = "Barbie"

ken = Doll()
ken.name = "Ken"

# print(barbie.material)
barbie.speak()
barbie.learn_new_language()

ken.speak()
ken.learn_new_language()