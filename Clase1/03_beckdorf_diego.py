def increment(index, carrie=False):
    if index is not None:
        index += 1
        if index == 25:
            return 0
        else:
            return index
    if index is None and carrie:
        return 0
    return None

def next(indexes):
    carrie = False
    while True:
        for i in range(4, -1, -1):
            indexes[i] = increment(indexes[i], carrie=carrie)
            carrie = False
            if indexes[i] == 0:
                carrie = True
            if carrie:
                continue
            break
        return indexes

def valid(indexes):
    aux = -1
    for i in indexes:
        if i is None:
            continue
        if i <= aux:
            return False
        aux = i
    return True

indexes = [None, None, None, None, 0]
alphabet = 'abcdefghijklmnopqrstuvxyz'
words = []
for _ in range(25**5):
    try:
        if valid(indexes=indexes):
            word = ''
            for index in indexes:
                if index is not None:
                    word += alphabet[index]
            words.append(word)
        indexes = next(indexes=indexes)
    except IndexError:
        break

file_name = input()
file = open(file_name)
for line in file:
    try:
        print(words.index(line) + 1)
    except Exception:
        print(0)
