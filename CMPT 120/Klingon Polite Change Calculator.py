#Klingon Polite Change Calculator
#This program takes the first user input as a purchase amount. THe second user input is the amount the user wishes to pay with. The program then uses an algorithem to figure out the best way to give back change to the user
#Made By: Jasper Quan
#Created: June 2, 2017
import unicodedata

currency = [90,30,10,1] #Iru = 90, Talon = 30, Darsak = 10, Shhhrok = 1
coinsBack = [0,0,0,0] #How much change to give, spots are relative to the currency list

print("Welcome to Klingon Polite Change Calculator!")

purchase = input("\nPlease, enter the purchase amount in mu (integer): ")
while purchase.isnumeric()==False:#check if user input is not a number
    purchase = input("\nPlease enter a NUMERIC amount for purchase: ")
purchase = int(purchase) 
if purchase < 0: #Check if purchased amount is negative, since you cannot buy negative amounts of stuff
    purchase = int(input("\nPurchase cannot be negative, please enter another amount: "))
    
pay = input("\nPlease, enter the amount paid by Klingon customer in mu to pay for purchase (integer): ")
while pay.isnumeric()==False: #check if the input entered by user is a number
    pay = input("\nPlease enter a NUMERIC amount for your payment: ")
pay = int(pay)
if pay < purchase: #Amount paid by customer must be atleast equal to amount due
    pay = int(input("\nPayment is not sufficient to cover cost, please enter a bigger payment: "))
    

change = pay - purchase 

for x in range(0,4): #Covers all index's in currency list
    if change >= currency[x]: #Checks if change is greater then value in currency index x
        coinsBack[x] = change // currency[x] #If so, see how many times currency value in index 'x' goes in change. Replace value in index 'x' in coinsBack list with number of times currency value 'x' fits in change
    change %= currency[x] #Calculate change remaining after subtracting change given back

print("\nThe Kling 'Polite' way to give back change of " + str(pay - purchase) + " mu is \n %i Iru, \n" %coinsBack[0], "%i Talon, \n" %coinsBack[1], "%i Darsek, \n" %coinsBack[2], "%i Shhhrok, \n\n ---Bye !---" %coinsBack[3])