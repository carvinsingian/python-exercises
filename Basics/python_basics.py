#importing
import utils
from utils import kg_to_lbs #imports specific function from module

#importing packages
import ecommerce.shipping
from ecommerce import shipping
from ecommerce.shipping import calc_shipping

#using path to get file
from pathlib import Path


#Class with constructor and to string method
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return f'{self.name} is {self.age}'


#Class initialization
class Animal:
	def walk(self):
		print("walk")


#Classes with inheritance
class Dog(Animal):
	def bark(self):
		print("bark")


#Dictionaries
def emoji_converter(message):
	words = message.split(' ')

	emojis = {
		':)': 'happy face',
		':(': 'sad face'
	}

	output = ''
	for word in words:
		output += emojis.get(word, word) + ' '

	return output


#Exceptions
def age_printer(age):
	try:
		age_int = int(age)
		income = 25000
		risk = income/age_int
		return risk
	except ValueError:
		return 'Invalid value'
	except ZeroDivisionError:
		return 'Age cannot be 0'


#Logic here
# age = input('>')
# print(age_printer(age))
# carvin = Person('Carvin', 23)
# print(carvin)

# array = []
# i = 0
# array_size = int(input('>array_size:'))

# while i < array_size:
# 	array.append(int(input(f'element {i+1}>')))
# 	i += 1

# print(utils.kg_to_lbs(70))
# print(kg_to_lbs(70))
# print(utils.find_max(array))

"""
Absolute path
Relative path
using Path

path.mkdir() creates a path
path.rmdir() removes a path
path.glob() search for files using a pattern
"""
path = Path()
for file in path.glob('*.*'):
	print(file)

