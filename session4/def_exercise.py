def exercise(number):
    print("홀수" if number % 2 else "짝수")

def exercise2(number):
    for i in range(1, 10):
        for j in range(1, 10):
            if(number % 2 and i % 2):
                print("{} x {} = {}".format(i, j, i*j))
            elif(number % 2 == 0 and i % 2 == 0):
                print("{} x {} = {}".format(i, j, i*j))

