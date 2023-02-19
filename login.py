def malumot():
    try:
        name = input("Ismingiz: ")
        familya = input("Familayangiz: ")
        pasport_seriya = int(input("Pasportingizni seriyasini kriting: "))
    except ValueError:
        print("Malumotingizni xato kritingiz!")

    with open("malumot.txt","w") as file:
        file.write(f" {name}\n {familya}\n Manashu {pasport_seriya} pasport seriyasi boyicha royxatdan otdi")

malumot()

