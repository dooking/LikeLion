# -*- coding: utf-8 -*-
# 즐거운 제어문 실습 시간 입니다

# 잘 안되시면 운영진께 질문 해주세요 ! 단, 질문 전에 스스로 아래 체크리스트 한번 확인 해주세요

# 0. 오타는 없는가?
# 1. 띄어쓰기는 잘했는가?
# 2. 들여쓰기는 잘했는가?

#######################################

print('\n')
print('#####################################')
print('#  즐거운 제어문 실습 시간 입니다~  #')
print('#####################################')
print('\n')
print('')

########################################
print('# 문제 1. 멋사 추합쟁이 준태 \n\n')

print('준태는 멋사 운영진에 뒤늦게 참여하였다. \n')
print('멋사 운영진 리스트를 복사하고, \n')
print('뒤늦게 참여한 준태를 멋사 운영진 명단에 추가하고, 반복문을 이용해 한 명씩 출력 해주세요!')

likelion_list = ['주원', '지환', '성우', '형제', '중훈', '경연', '상하']

fixed_likelion_list = []
print('\n\n')
for likelion in likelion_list:
    fixed_likelion_list.append(likelion)
    print(likelion, end = ' ')
fixed_likelion_list.append('준태')
print(fixed_likelion_list[-1])


print('\n\n')
print('################################### \n')
print('# 문제 2. 중훈이 따돌리기  \n\n')
print('완성된 멋사 운영진 리스트에서 문자열 실습할 때 까탈스럽게 군 중훈이를 빼고 나머지 사람들에게 형제집 닭갈비를 사주고싶다. \n')
print('while 문이나 for 문, if 문, 포매팅을 활용하여 중훈을 제외한 나머지 운영진에게 형제집 닭갈비를 사주세요! \n')
print('* 출력 예시(문자열로) : 주원에게 형제집 닭갈비를 사주었습니다! ')
for likelion in likelion_list:
    if(likelion == "중훈"):
        continue
    print(f"{likelion}에게 형제집 닭갈비를 사주었습니다!")

print('\n\n')