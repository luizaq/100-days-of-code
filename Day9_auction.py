from replit import clear
import logo

bonecos = {}
continuar = True
print(f"wlcome to the silent auction!\n {logo}")
while continuar:
    name = input("Please type tour name: \n")
    bid = input("Please type your bid: \n")
    int(bid)
    opt = input("more people? type 'yes' or 'no'\n")
    if opt == "y":
        #clear()
        continuar = True
    elif opt == "n":
        continuar = False
    else:
        print("???")
        break
    bonecos[name] = bid
lista_keys = list(bonecos.keys())
lista_values = list(bonecos.values())
vmax = max(lista_values)
kmax = lista_values.index(vmax)
print (f"Ganhador : {lista_keys[kmax] } com o valor : { vmax}")
