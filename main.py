from login import *

def uzb_ayraprti():
    print('''
    Assalomu aleykum! Uzbekistan xavo yo'llari aviya kampaniyamizga xush kelibsiz! 
    Siz bu yerda chiptani  online xarid qilishingiz mumkun!''')
    shahar = ["Andijon", "Farg'ona", "Namangan", "Samarqand", "Buxoro", "Navoiy", "Qoraqalpoq"]
    with open("malumot.txt","r") as file:
        file.readlines()
    while True:
        try:
            print(shahar)
            x = input(f"Qaysi shaharga uchishni istaysiz: ")
            if x == "Andijon":
                cipta_narxi = 230000
                print(f"Mijoz  siz xoxlagan {x} shahriga chipta narxi {cipta_narxi} so'm")
                sotib_olish = int(input('''Chipta xarid qilishni istaysizmi?
                HA uchun 1 ni bosing
                YO'Q uchun 2 ni bosing: '''))

                if sotib_olish == 1:
                    print(f"Sizdan {cipta_narxi} so'm bo'ldi ")
                    break
                else:
                    print("Raxmat")
                    break

            elif x == "Farg'ona":
                cipta_narxi = 230000
                print(f"Mijoz  siz xoxlagan {x} shahriga chipta narxi {cipta_narxi} so'm")
                sotib_olish = int(input('''Chipta xarid qilishni istaysizmi?
                HA uchun 1 ni bosing
                YO'Q uchun 2 ni bosing: '''))

                if sotib_olish == 1:
                    print(f"Sizdan {cipta_narxi} so'm bo'ldi ")
                    break
                else:
                    print("Raxmat")
                    break

            elif x == "Namangan":
                cipta_narxi = 230000
                print(f"Mijoz  siz xoxlagan {x} shahriga chipta narxi {cipta_narxi} so'm")
                sotib_olish = int(input('''Chipta xarid qilishni istaysizmi?
                HA uchun 1 ni bosing
                YO'Q uchun 2 ni bosing: '''))

                if sotib_olish == 1:
                    print(f"Sizdan {cipta_narxi} so'm bo'ldi ")
                    break
                else:
                    print("Raxmat")
                    break

            elif x == "Samarqand":
                cipta_narxi = 230000
                print(f"Mijoz  siz xoxlagan {x} shahriga chipta narxi {cipta_narxi} so'm")
                sotib_olish = int(input('''Chipta xarid qilishni istaysizmi?
                HA uchun 1 ni bosing
                YO'Q uchun 2 ni bosing: '''))

                if sotib_olish == 1:
                    print(f"Sizdan {cipta_narxi} so'm bo'ldi ")
                    break
                else:
                    print("Raxmat")
                    break

            elif x == "Buxora":
                cipta_narxi = 230000
                print(f"Mijoz  siz xoxlagan {x} shahriga chipta narxi {cipta_narxi} so'm")
                sotib_olish = int(input('''Chipta xarid qilishni istaysizmi?
                HA uchun 1 ni bosing
                YO'Q uchun 2 ni bosing: '''))

                if sotib_olish == 1:
                    print(f"Sizdan {cipta_narxi} so'm bo'ldi ")
                    break
                else:
                    print("Raxmat")
                    break
            elif x == "Navoiy":
                cipta_narxi = 230000
                print(f"Mijoz  siz xoxlagan {x} shahriga chipta narxi {cipta_narxi} so'm")
                sotib_olish = int(input('''Chipta xarid qilishni istaysizmi?
                HA uchun 1 ni bosing
                YO'Q uchun 2 ni bosing: '''))

                if sotib_olish == 1:
                    print(f"Sizdan {cipta_narxi} so'm bo'ldi ")
                    break
                else:
                    print("Raxmat")
                    break

            elif x == "Qoraqalpoq":
                cipta_narxi = 230000
                print(f"Mijoz  siz xoxlagan {x} shahriga chipta narxi {cipta_narxi} so'm")
                sotib_olish = int(input('''Chipta xarid qilishni istaysizmi?
                HA uchun 1 ni bosing
                YO'Q uchun 2 ni bosing: '''))

                if sotib_olish == 1:
                    print(f"Sizdan {cipta_narxi} so'm bo'ldi ")
                    break
                else:
                    print("Raxmat")
                    break
        except:
            print("Biz faqat Uzbekiston ichidagi shaharlarga chipta sotamiz")
            qayta_urinish = input('''
                    Biznig kampaniyadan yana bir bor chipta sotib olishni istaysizmi?
                    Ha uchun 1 ni bosing
                    YO'Q ucun 2 ni bosing: ''')
            if qayta_urinish == 2:
                break

uzb_ayraprti()
