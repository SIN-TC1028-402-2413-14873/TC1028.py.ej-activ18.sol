def main():
    #escribe tu código abajo de esta línea
    n = int(input(">>>"))
    m = int(input(">>>"))

    if n < 2:
        print("Error!")
    elif m < 2:
        print("Error!")
    else:
        matriz=[]
        dato = 1

        for row in range(n):
            renglon=[]
            for column in range(m):
                renglon.append(dato)
                dato = dato + 1
            matriz.append(renglon)
        print(matriz)


if __name__=='__main__':
    main()
