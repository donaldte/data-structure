list = [3, 44, 6, 6, 8, 9, 54, 445, 3]
pos = -1


def search(liste, a):
    i = 0
    while i < len(liste):
        if liste[i] == a:
            globals()['pos'] = i
            return True
        i += 1
    return False


n = 44
if search(list, n):
    print("Found at ", pos+1)
else:
    print("Not Found")
