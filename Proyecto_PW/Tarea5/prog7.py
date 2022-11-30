import random
random = random.randint(1, 10)

def main():
    var = int(input("Ingresa un número:"))
    if var == random:
        print("Adivinaste")
    else:
        print("Vuelve a Intentar")
        main()

main()
