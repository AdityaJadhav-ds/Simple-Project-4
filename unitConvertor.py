print(".......WELLCOME TO UNIT CONVERTOR.......")

list = { 1 : "Celsius to Fahrenheit\n", 2 : "Kilograms to Pounds\n", 3 : "Kilometers to Miles\n"}

print('''
1. Celsius to Fahrenheit
2. Kilograms to Pounds
3. Kilometers to Miles\n''')

while True :
    chose = int(input("Chose the option :  \n"))
    if chose < 4 : 
        break
    else : 
        print(" Chose between 1 to 3, Try Again ⚠️\n")

for i in list : 
  if chose == 1 : 
    Celsius = int(input("\nEnter Celsius : \n"))
    print(f" \n...............Converting celsius to fahrenhiet................\n \n Fahrenhiet = {(Celsius * 9/5)+32} AF\n")
    break
  if chose == 2 : 
    kg = int(input("\nEnter Kilograms : \n"))
    print(f" \n...............Converting kilogram to pound.................\n \n Pounds = {kg * 2.20462} lbs \n")
    break
  if chose == 3 : 
    Kilometers = int(input("\nEnter Kilometers : \n"))
    print(f" \n...............Converting kilometer to miles................ \n \n Miles = {Kilometers * 0.621371} miles\n")
    break 
  else : 
     print("Something want Wrong, Please try again Later ⚠️⛔")
