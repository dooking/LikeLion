def gugudan_odd():
    i = 1
    while i < 10:
        for j in range(1, 10):
            print("{} x {} = {}".format(i, j, i*j))
        i += 2
def gugudan_even():
    i = 2
    while i < 10:
        for j in range(1, 10):
            print("{} x {} = {}".format(i, j, i*j))
        i += 2
def gugudan_odd_or_even(n):
    if(n % 2):
        gugudan_odd()
    else:
        gugudan_even()

gugudan_odd_or_even(4)