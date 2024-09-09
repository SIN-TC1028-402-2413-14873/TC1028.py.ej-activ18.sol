def main():
    renglon1=input(">>>")
    renglon2=input(">>>")

    lista1 = renglon1.split()
    lista2 = renglon2.split()

    if len(lista1) != 2:
        print("Error!")
    elif len(lista2) != 2:
        print("Error!")
    else:
        matriz=[]
        matriz.append(lista1)
        matriz.append(lista2)

        print(matriz)

        determinante=int(matriz[0][0]) * int(matriz[1][1]) - int(matriz[0][1]) * int(matriz[1][0])

        print(f"determinante={determinante}")


if __name__=='__main__':
    main()
