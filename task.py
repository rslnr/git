# 1
a = 5
for i in range(a):
        for b in range(a):
            if i == 0 or i == a - 1 or b == 0 or b == a - 1:
                print("*", end = "  ")
            else:
                print(" ", end = "  ")
        print()
##############################################################
# 2
print()
a = 3
c = 7
for i in range(a):
        for b in range(c):
            if i == 0 or i == a - 1 or b == 0 or b == a + 3:
                print("*", end = "  ")
            else:
                print(" ", end = "  ")
        print()
##############################################################
# 3
print()
a = 7
c = 3
for i in range(a):
        for b in range(c):
            if i == 0 or i == a - 1 or b == 0 or b == a - 5:
                print("*", end = "  ")
            else:
                print(" ", end = "  ")
        print()
##############################################################
# 4
print()
a = 6
for i in range(a, 0, -1):
    for b in range(a - i):
        print(" ", end = "")
    for b in range(2 * i - 1):
        print("*", end = "")
    print()
for i in range(2, a + 1):
    for b in range(a - i):
        print(" ", end = "")
    for b in range(2 * i - 1):
        print("*", end = "")
    print()

