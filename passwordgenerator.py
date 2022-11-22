import random as r


print("passcode generator")

#wordlist
wordlist = [ 'new', 'awesome', 'hello', 'python', 'strings', 'statements', 'code', 'vulnerability' ]

#changes max word whatever to the amount of inputs
maxword = len(wordlist) - 1

#numbers for numlist
num1 = r.randint(0,1000)
num2 = r.randint(0,1000)
num3 = r.randint(0,1000)
num4 = r.randint(0,1000)
num5 = r.randint(0,1000)
num6 = r.randint(0,1000)

#numlist
numlist = [ num1, num2, num3, num4, num5, num6 ]

#numlist minus one to give maximum list item
maxnum = len(numlist) - 1

#choose one of the items from the list, with a maximum of 'maxword' or 'maxnum'
one = r.randint(0,maxword)
two = r.randint(0,maxword)
three = r.randint(0,maxnum)
four = r.randint(0,maxnum)

#prints an error if a password isnt actually created:
password = "ERROR"

#self explanatory really
repeat = input("press r for new password ")

#if input is r, run this:
while repeat == 'r':
	#concatenates words and numbers
	print( "yes " + str(one) + " " + str(three) + " " + str(two) + " "+ str(four))
	
	while one == two:
		two = r.randint(0,1000)
	password = wordlist[one] + str(numlist[three]) + wordlist[two] + str(numlist[four])
	#print out password
	print("password: " + password)
	#after input is put in, while loop keeps going unless repeat != r
	repeat = input("press r for new password")
	#redefines all variables
	one = r.randint(0,maxword)
	two = r.randint(0,maxword)
	three = r.randint(0,maxnum)
	four = r.randint(0,maxnum)
	num1 = r.randint(0,1000)
	num2 = r.randint(0,1000)
	num3 = r.randint(0,1000)
	num4 = r.randint(0,1000)
	num5 = r.randint(0,1000)
	num6 = r.randint(0,1000)

	while one == two:
		two = r.randint(0,maxword)
	while three == four:
		four = r.randint(0,maxnum)
	 