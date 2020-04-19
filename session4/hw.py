def hw1():
    for i in range(9,0,-1):
        print("*"*i)
def hw2():
    for i in range(10):
        print("2 x {} = {}".format(i,2*i))
def hw3():
    sum_i = 0
    i=1
    while i<=1000:
        if(i%3):
            sum_i+=i
        i+=1
    print(sum_i)
def hw4():
    mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
    avg_mutsa =0
    for i in mutsa_scores:
        avg_mutsa += i
    print(avg_mutsa/len(mutsa_scores))
def hw5():
    print("전화번호 받기 : ",end ='')
    phone_number = ''.join(str(input()).replace(" ","").replace(",", "").replace(".","").split("-"))
    print("전화번호 출력 :",phone_number)
    print("영어 이름 받기 : ",end ='')
    first_name,last_name = map(str,input().split())
    print(f'first name : {first_name.title()}, last_name : {last_name.title()}')
