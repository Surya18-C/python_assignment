
def split_remove_duplicates(str,n):

    result=[]
    for i in range(0,len(str),n):

        split_str=str[i:i+n]

        result.append(split_str)

    return result

