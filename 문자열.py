fruit = 'banana'
index = 0

# while 루프

while index < len(fruit) : # len() 내장함수 : 문자의 길이
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# 0 b
# 1 a
# 2 n
# 3 a
# 4 n
# 5 a

# for 루프

for letter in fruit 
print(letter)

#------------------------------------

name = input('Enter: ') # input() 내장함수 : 사용자로 부터 키보드 입력을 받음
print(type(name))   #type() 내장함수 :주어진 변수나 값의 자료형을 반환
print(name)

# > Enter: 123 으로 입력합니다.
# 인풋값 123의 타입은 <class 'str'>과 같습니다.
# 123으로 출력됩니다.

#-----------------------------------------------------------------
#문자열 슬라이싱
myString = 'Monty Python'
print(myString[0:4])
# Mont가 출력됩니다. 여기서 0 to 4에서 4에 대한 인덱스는 출력되는 값에 포함되지 않는 것을 확인하여야 합니다.
print(myString[6:7])
# P가 출력됩니다.
print(myString[6:20])
# Python이 출력됩니다.
print(myString[:2])
# index값이 2에 해당하는 문자 앞부터 출력됩니다.
print(myString[8:])
# index값이 8에 해당하는 문자부터 출력됩니다.
print(myString[:])
# 전체가 출력됩니다.

#문자열 합치기
firstString = 'Hello'
secondString = 'There'
print(firstString + secondString)
# HelloThere로 출력됩니다.
thirdString = firstString + ' ' + secondString
print(thirdString)
# Hello There로 출력됩니다.

#in 활용 (in : 문자가 있는지 없는지 확인)

#fruit = 'banana'
print('n' in fruit)
# True로 출력됨
print('m' in fruit)
# False로 출력됨
print('nan' in fruit)
# True로 출력됨
if 'a' in fruit :
    print('Found it!')
# Found it으로 출력됨
    

'''
Strip 메소드

문자열에서 공백을 제거할 수 있는 메소드가 존재합니다. 

lstrip(): 왼쪽 공백 제거

rstrip(): 오른쪽 공백 제거

strip(): 오른쪽 왼쪽 공백 제거
'''

greet = '                     Hello Bob       '
greet.lstrip()
# 왼쪽의 공백이 삭제됨
greet.rstrip()
# 오른쪽의 공백이 삭제됨
greet.strip()
# 양쪽의 공백이 삭제됨

#str은 문자열 타입을 가리키는 파이썬의 예약어#

#start with 메소드

line = 'Please have a nice day'
print(line.startswith('Please'))
# True가 출력됨
print(line.startswith('p'))
# False가 출력됨 : 대소문자 구분


