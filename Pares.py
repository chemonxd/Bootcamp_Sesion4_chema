
if __name__ == '__main__':

    print("ingrese un valor inicial menor que el valor final")
    num_initial = int(input())
    print("ingrese un valor final mayor que el valor inicial")
    num_final = int(input())
    num_odd = []

    if num_initial <= num_final:
        for i in range(num_initial, num_final + 1):
            if i % 2 != 0:
                num_odd.append(i)
    else:
        print("El valor final debe de ser mayor")

    print(num_odd)
