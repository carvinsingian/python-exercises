import random


class Dice:
	def roll(self):
		first = random.randint(1,6)
		second = random.randint(1,6)

		return first, second


for i in range(3):
	print(random.random())

for i in range(3):
	print(random.randint(10,20))


members = ['Carvin', 'Joseph', 'Kyle']
leader = random.choice(members)
print(leader)

dice = Dice()
print(dice.roll())




