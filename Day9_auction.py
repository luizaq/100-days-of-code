from replit import clear
import logo


bonecos= {}
continuar = True

print(f"wlcome to the silent auction!\n {logo}")
while continuar:
    name = input("Please type tour name: \n")
    bid = input("Please type your bid: \n")
    int(bid)
    opt = input("more people? type 'yes' or 'no'\n")
    if opt == "yes":
        clear()
        continuar = True
    elif opt == "no":
        continuar = False
    else:
        print("???")
    bonecos[name] = bid

vmax = max(bonecos.values())

for boneco, bid in bonecos.items():
    if bid == vmax:
        clear()
        print(f"The winner is{boneco} with a bid of {bid}")


