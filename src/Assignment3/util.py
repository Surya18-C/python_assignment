
#Mutations

def mutation():
    str_val = "Apple"

    # Convert the string to a list of characters
    lis = list(str_val)

    # Modify the specific character in the list
    lis[4] = 'A'

    # Join the list back into a string
    new_str = ''.join(lis)

    # Print the modified string
    return new_str

