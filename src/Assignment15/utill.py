
def count():
    para = "hello All welcome to the class"

    # count letters

    count = 0

    for i in para:
        count += 1


    # count words

    split_word = para.split()

    return "Total words", len(split_word) , "Total letters", count