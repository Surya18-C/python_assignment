
def min_max():
    n = int(input("Enter n : "))

    data = [list(map(int, input().split())) for _ in range(n)]

    min_value = []

    for i in data:
        min_value.append(min(i))

    result = max(min_value)

    return result