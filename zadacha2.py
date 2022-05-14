if __name__ == '__main__':

    x = list(map(float, input("Введите элементы списка: ").split()))
    c = float(input("Введите С: "))
    k, sum = 0, 0
    j = 0

    for i in x:
        if i < c:
            k += 1
        if i < 0:
            j = k

    for i in range(j, len(x)):
        #print(j)
        sum += int(x[i])

    print("Количество элементов списка, меньших С: ", k)
    if j == 0:
        print("Нет отрицательного числа в списке.")
    else:
        print("Cумма целых частей элементов списка, расположенных после последнего отрицательного элемента: ", sum)

