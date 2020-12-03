# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

n1=name1.lower()
n2=name2.lower()


t=n1.count("t")
r=n1.count("r")
u=n1.count("u")
e=n1.count("e")
true_count1=t+r+u+e


t=n2.count("t")
r=n2.count("r")
u=n2.count("u")
e=n2.count("e")

true_count2=t+r+u+e

true_count_total=true_count+true_count2
#love
l=n1.count("l")
o=n1.count("o")
v=n1.count("v")
e=n1.count("e")

love_count1=l+o+v+e

l=n2.count("l")
o=n2.count("o")
v=n2.count("v")
e=n2.count("e")

love_count2=l+o+v+e

love_count_total=love_count1+love_count2

score = love_count_total+ true_count_total

if score <10 or score>90:
  print (f"Your score is {score}, you go together like coke and mentos.")

elif score >=40 or score <=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print (f"your score is {score}")




