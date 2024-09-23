
def unique_element():
    a = [1, 2, 1, 4, 3, 4, 5, 4, 6]

    unique_element = []

    for i in a:
        if i not in unique_element:
            unique_element.append(i)

    return unique_element

