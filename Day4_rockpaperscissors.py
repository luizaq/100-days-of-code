rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
escolha=input(" Escolha 0 para pedra, 1 para papel,2 para tesoura")

escolha=int(escolha)

import random

escPc=random.randint(0,3)

if escolha==0 and escPc==0:
  print(f"Empate!\n pc escolheu  {rock} \n player escolheu: {rock}")
elif escolha==1 and escPc==1:
  print(f"Empate!\n pc escolheu  {paper} \n player escolheu: {paper}")
elif escolha==2 and escPc==2:
    print(f"Empate!\n pc escolheu  {scissors} \n player escolheu: {scissors}")
elif escolha==0 and escPc==1:
  print (f"PC ganha!!! \n pc escolheu {paper}\n player escolheu {rock} ")
elif escolha==0 and escPc==2:
  print (f"PC ganha!!! \n pc escolheu {scissors}\n player escolheu {rock} ")
elif escolha==1 and escPc==0:
    print (f"Player ganha!!! \n pc escolheu {rock}\n player escolheu {paper} ")
elif escolha==1 and escPc==2:
   print (f"PC ganha!!! \n pc escolheu {scissors}\n player escolheu {paper} ")
elif escolha==2 and escPc==0:
     print (f"PC ganha!!! \n pc escolheu {rock}\n player escolheu {scissors} ")

elif escolha==2 and escPc==1:
    print (f"Player ganha!!! \n pc escolheu {paper}\n player escolheu {scissors}")
else:
  print("erro")
