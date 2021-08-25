def sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


list = [4, 5, 7, 75, 775, 567, 789, 654, 4321]
sort(list)
print(list)
