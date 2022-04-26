for i in range(10):
    for j in range(i + 1, 10):
        print(i, end="")
        if (j == 9 and i == 8):
            print(j)
        else:
            print(j, end=", ")
