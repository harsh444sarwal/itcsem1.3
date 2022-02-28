#QUESTION 1.
def TOH(n , fromrod, torod, middlerod):
	if n == 0:
		return
	TOH(n-1, fromrod, middlerod, torod)
	print("Move disk",n,"from rod",fromrod,"to rod",torod)
	TOH(n-1, middlerod, torod, fromrod)
n = 3
TOH(n, 'A', 'C', 'B')
print("\n")

#QUESTION 2.
from math import factorial, remainder
from tracemalloc import start
n=int(input('size of pascals triangle u want '))

print("loops method")
for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")
print("recurssions method")
def pascalstriangle(n,originalength=n):
    if n == 0:
        return
    pascalstriangle(n-1,originalength)
    #print spaces
    print('  '*(originalength-n), end='')
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #use Binomial Coefficient
        start = start * (n - i) // i
    print()
pascalstriangle(n)
print("\n")

#QUESTION 3.
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number(not zero): "))
quotient=num1//num2
remainder=num1%num2

def check0(input):
    if input ==0:
        print()

#part a
print("Part A")

print("Checking if callable or not!")
print("Quotient:",callable(quotient))
print("Remainder:",callable(remainder))
print()
#part b

print("Part B:")
if (num1 and num2 and quotient and remainder)!=0:
    print("All values are non zero!!")

elif num1 == 0 or num2 == 0 or quotient == 0 or remainder == 0:
    print("Not all values are non zero")
print()
#part c        
print("Part C")

displaylist=[num1,num2,quotient,remainder]
displaylist= displaylist+[4,5,6]
for i in displaylist:
    if i>4:
        print(i)

print("Done")        
print()
#part D
print("Part D")
setdata=set(displaylist)
print("Done")
print("Set is",setdata)
print()
#part E
print("Part E")
immutableset=frozenset(setdata)
print("Done")
print(immutableset)
print()
#Part F
print("Part F")
print("Hash value of maximum of set:",(hash(max(immutableset))))

#QUESTION 4.
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("destroyed object")

#create object
student1 = Student('naman', 123456)
print("created object")
#print the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.roll_no}.")
#delete the object
del student1
print("\n")


#QUESTION 5.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part a updating salary
employee1.salary = 70000
print("The updated salary of",employee1.name ,"is",employee1.salary)
#part b deleting a record
print("<b>Record of Viren deleted")
del employee3
print("\n")


#QUESTION 6.
print("welcome to friendship test game")
#let the first friend enter their word
word =input("Enter word please: ")
word=word.lower()

#inputting a meaningful word with the exact same letters
testword = input("please enter one meaningful word using the exact same letters")
testword=testword.lower()
#define a dictionary
def countdict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#let the shopkeeper check if thw words make sense
def finput():
    if countdict(word) != countdict(testword):
        print("letters dont match, fake friendship")
        return
    ask = input("Do these words make sense?(y/Y or n/N )")

    if ask == 'y' or ask=='Y':
        print("u friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("no meaningful words, fake friendship")
    else:
        print("try again: y/Y or n/N ")
        finput()
finput()
