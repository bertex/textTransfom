import transfom


def main():
    string = input("Introdueix un string:")

    print("Quina transformació vols?")
    print("[1] Text amb tot majuscules")
    print("[2] Text amb tot minúscuies")
    print("[3] Text capitalitzat ")

    opcio = input("opció escollida: ")

    if opcio == "1":
        print(transfom.to_upper_case(string))
    elif opcio == "2":
        print(transfom.to_lower_case(string))
    elif opcio == "3":
        print(transfom.to_capitalize(string))
    else:
        print("opció no reconegudda")


if __name__ == '__main__':
    main()
