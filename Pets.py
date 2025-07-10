class Pets:
    def make_sound(self):
        pass
class cat(Pets):
    def make_sound(self):
        print("meow")
class Dog(Pets):
    def make_sound(self):
        print("woof")
for v in [cat(),Dog()]:
    v.make_sound()