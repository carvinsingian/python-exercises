#runner up challenge

def runner_up(scores):
	pass

n  = int(input('>'))
arr = map(int, input().split())

number_list = list(arr)
number_list.sort(reverse = True)
runner_up = 0

for i in range(len(number_list)):
	if number_list[-i-1] != max(number_list):
		runner_up = number_list[-i-1]

print(runner_up)


	