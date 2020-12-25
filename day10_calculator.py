def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


ops = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
continua = True
# o dic aponta a funcap
# key = *+_/
# value = names
while continua:

    num1 = float(input("Type the first number"))
    for sym in ops:
        print(sym)
    operation_symbol = input("Pick an operation from above")
    num2 = float(input("Type the second number"))

    func = ops[operation_symbol]
    answer = func(num1, num2)

    cont = input("continue?  y or n or restart")
    cont = cont.lower()

    if cont == "y":
        num1 = answer

    elif cont == "n":
        print("ok")
        continua = False

    elif cont== "r":
     print("reiniciando...")
    else:
        print("ok")
        continua = False

# transf answer no num 1

# verificar op
# chamar func
# # Answer = ret fun
# if opt == "+":
#     answer = add(num1, num2)
# elif opt == "-":
#     answer = sub(num1, num2)
# elif opt == "*":
#     answer = mp(num1, num2)
# elif opt == "/":
#     answer = dvd(num1, num2)
# else:
#     print("erro")


print(f"{num1} {operation_symbol} {num2} = {answer}")

# for i in ops:
#  print(ops.keys())
# cria uma lista de keys
