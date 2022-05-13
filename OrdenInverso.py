
if __name__ == '__main__':
    numbers = []
    numbers_inverted = []

# ingresamos los números del 1 al 100 en una lista
    for i in range(1, 100 + 1):
        numbers.append(i)
# Utilizamos la función sorted para invertir la lista numbers
    numbers_inverted = sorted(numbers, reverse=True)

    print(numbers_inverted)
