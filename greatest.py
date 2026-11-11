FirstNumber=int(input("Enter the first Number"))
SecondNumber=int(input("Enter the Second Number"))
ThirdNumber=int(input("Enter the Third Number"))
FourthNumber=int(input("Enter the Fourth Number"))

if FirstNumber<SecondNumber:
    FirstNumber=SecondNumber
if FirstNumber<ThirdNumber:
    FirstNumber=ThirdNumber
if(FirstNumber<FourthNumber):
    FirstNumber=FourthNumber

print("The max of entered numbers is: ",FirstNumber)