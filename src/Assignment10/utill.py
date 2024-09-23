
def cnt(n):
    val = []

    count = {}

    for i in n:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    counts=[]
    for k, v in count.items():
         counts.append(v)

    return counts

