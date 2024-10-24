# Write code below 💖

# Write code below 💖

class Pokemon():
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
  def speak(self):
    print(self.name +" "+ self.name)
  def display_details(self):
    if self.is_caught == True:
          print('Entry: ' + str(self.entry))
          print('Name: ' + str(self.name))
          print('Type: ' + str(self.types))
          print('Description: ' + str(self.description))
          print(str(self.name) + ' has been caught!')
    else:
          print('Entry: ' + str(self.entry))
          print('Name: ' + str(self.name))
          print('Type: ' + str(self.types))
          print('Description: ' + str(self.description))
          print(str(self.name) + ' has not been caught ;(')

Bulbasaur = Pokemon(1, 'Bulbasaur', 'Grass', 'It uses the nutrients that are packed into the seed', True)
Bulbasaur.speak()
Bulbasaur.display_details()
print("===================")

Charizard = Pokemon(6, 'Charizard', 'Fire', 'It breathes flames from its mouth', False)
Charizard.speak()
Charizard.display_details()
print("===================")

Metapod = Pokemon(11, 'Metapod', 'Bug', 'it can only harden, remains motionless', True)
Metapod.speak()
Metapod.display_details()
print("===================")

