# Example from: https://www.codeunderscored.com/python-classes-and-objects-with-examples/


# program showing the variables with the value assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance variables.

# Class for Cow
class Cow:

	# Class Variable
	animal = 'cow'

	# The init method or constructor
	def __init__(self, breed, color):

		# Instance Variable
		self.breed = breed
		self.color = color

# Objects of Cow class
jersey = Cow("Jersey", "black")
guernsey = Cow("Guernsey", "brown")

print('Jersey details:')
print('Jersey is a', jersey.animal)
print('Breed: ', jersey.breed)
print('Color: ', jersey.color)

print('\nGuernsey details:')
print('Guernsey is a', guernsey.animal)
print('Breed: ', guernsey.breed)
print('Color: ', guernsey.color)

# variables in a class accessed using the class's name
print("\nAccessing class variable using class name")
print(Cow.animal)

