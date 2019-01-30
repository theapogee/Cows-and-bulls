import random as rd
def four_digit_gen():
	right_number=[]
	counter = 0
	while counter < 4:
		y = rd.randint(0,9)
		if y not in right_number:
			right_number.append(y)
			counter += 1

	return right_number
	print (right_number)




def cows(right_number):
	print (right_number)

	while True:
		counter = 0
		counter += 1
		user_input = input('Guess the 4 digit number: ')
		user_number = [int(x) for x in user_input]
		cows = 0
		bulls = 0
		for element in user_number:
			if element in right_number:
				if user_number.index(element) == right_number.index(element):
					cows += 1
		print ("Cows = %s" %cows)
		if cows == 4:
			print ('You have won')
			break

		for element in user_number:
			if element in right_number:
				bulls += 1
		print ("Bulls = %s" %bulls)








cows(four_digit_gen())



