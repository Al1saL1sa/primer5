if __name__ == '__main__':

    x = list(map(int, input("Введите 10 элементов: ").split()))
    k = 0

    for i in x:
       if (((i) ** 2) % 4 == 0):
        k +=1

    print("Количество квадратов элементов кратных 4: ", k)
