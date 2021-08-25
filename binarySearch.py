pos = -1


def search(list, n):
    l = 0
    u = len(list)
    while l < u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        elif list[mid] < n:
            l = mid + 1
        else:
            u = mid - 1
    return False


list = [4, 5, 7, 75, 775, 567, 789, 654, 4321]
n = 9
if search(list, n):
    print("Found", pos + 1)
else:
    print("Not Found")
