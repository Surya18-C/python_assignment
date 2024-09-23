def sub_set():
    a = list(map(int, input("Enter list values: ").split()))  # List of integers

    A = set(map(int, input("Enter set A values: ").split()))  # Set A
    B = set(map(int, input("Enter set B values: ").split()))  # Set B

    total = 0

    for i in a:
        if i in A:
            total += 1
        elif i in B:
            total -= 1

    return total


print(sub_set())
