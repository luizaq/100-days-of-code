#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print ("Welcome to the top calculator\n")

total=input ("What was the total of the bill? $ \n")
per=input("what percentage tipo would you like to give? 10,12,15,or 12 \n")
people=input("How many people to split the bill? \n")

totalF=float(total)
perI=int(per)
peopleI=int(people)

tip=totalF*(perI/100)
result=(totalF+tip)/peopleI

print(f"Each person should pay: {result}")
