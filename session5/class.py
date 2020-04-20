class FourCal:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        self.add_count = 0
        self.sub_count = 0
        self.mul_count = 0
        self.div_count = 0
    def add(self, n1, n2):
        self.add_count += 1
        return n1 + n2
    def sub(self, n1, n2):
        self.sub_count += 1
        return n1 - n2
    def mul(self, n1, n2):
        self.mul_count += 1
        return n1 * n2
    def div(self, n1, n2):
        if (not n2):
            print("0으로 나눌 수 없습니다")
            return None 
        self.div_count += 1
        return n1 // n2
    def ShowCount(self):
        print("덧셈 : ",self.add_count)
        print("뺄셈 : ",self.sub_count)
        print("곱셈 : ",self.mul_count)
        print("나눗셈 : ",self.div_count)

cal = FourCal("김동현", 24,"korea")
print(cal.add(3,4))
print(cal.sub(3,4))
print(cal.mul(3,4))
print(cal.ShowCount())
