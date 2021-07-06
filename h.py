'''def cube(num):
	return num*num*num
print(cube(199))'''



'''def greatest(num1 , num2 , num3 ):
	if num1 >= num2 and num1 >= num3:

	    return num1
	elif num2 >= num3 and num2 >= num3:
	    return num2
	else:
	    return num3

print(greatest (100,57,43))'''




'''from u import student
student1 = student("harry", "social studies", 9, True )
student2 = student("adi", "computer", 8, True )
student3 = student("ravi", "arts", 7, False )
student4 = student("happy", "business", 8, False )
print(student3.gpa)'''
'''
from emoji import emojize
print(emojize(":thumbs_up:"))


'''
'''howdoi use Howdoi in Python
from emoji import emojize
print(emojize(":rose:"))'''


'''def min(num1, num2, num3):
	if num1<=num2 and num1<=num3:
	    return num1
	elif num2<=num1 and num2<=num3:

	    return num2
	else:
		return num3
print(min(6,7,8))'''


'''num1 = float(input("enter first number:"))
operation = input("enter the operator:")
num2 = float(input("enter second number:"))
if operation == "+" :
	print(num1+num2)
elif operation == "-":
	print(num1-num2)
elif operation == "*":
	print(num1*num2)
elif operation == "/":
	print(num1/num2)
elif opertaion == "%":
	print(num1%num2)
else:
	print("tum chutiya ho")'''

'''
month = {
"jan":"JANUARY", "feb":"FEBRUARY", "mar":"MARCH","apr":"APRIL","may":"MAY","jun":"JUNE","jul":"JULY","aug":"AUGUST","sept":"SEPTEMBER","oct":"OCTOBER","nov":"NOVEMBER","dec":"DECEMBER"

}
print(month.get("xyz"))'''

'''
i = 1
while i <= 10:
	print (i)
	i += 1
print("well done")'''
print ("HINT : Gunda")
limit = 3
guess_word = "don"
count = 0
didwin = False
while count<limit :
	guess = input("enter the word: ")
	count += 1
	if guess == guess_word:
		print("You won it")
		didwin = True
		break
if didwin == False:
        print("hey, u are dumb")







