#while 루프
n = 5

while n > 0: # -- : 사용
    print(n)
    n = n - 1


while True:
    line = input('> ')
    if line[0] == '#' :
        continue # continue를 만나면 while 루프가 처음으로 돌아가 루프 다시 실행
    if line == 'done' :
        break
    print(line) # break을 만나면 while 루프 종료되고 다음의 명령어 실행
print('Done!')

#input() 함수를 사용하면 사용자로부터 키보드 입력을 받을 수 있다. >는 입력을 요청하는 프롬포트 (사용자가 >뒤에 입력하고 엔터를 누르면 line 변수에 저장)

# ----------------------------------

#for 루프

#예시 1
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')

# 5
# 4
# 3
# 2
# 1
# Blastoff!

#예시 2

friends = ['Connect', 'Korea', 'NHN']
for friend in friends:
    print('Happy New Year!! ', friend)
print('Done!')
# Happy New Year!!  Connect
# Happy New Year!!  Korea
# Happy New Year!!  NHN
# Done!

#------------------------------------


#반복문

#가장 큰 수를 찾아내는 코드
largest_so_far = -1 # 값을 가지고 있는 변수를 선언해 줍니다. 작은 수로 -1로 선언을 합니다.
print('Before', largest_so_far) # 최초의 값과 루프 이후의 값을 비교하기 위해 print 함수로 현재의 값을 확인 합니다.
numbers = [9, 41, 12, 3, 74, 15] 
for the_num in numbers :
    if the_num > largest_so_far : # iteration value의 현재의 값(the_num)이 현재 가장 큰 값이 할당 되어 있는 largest_so_far보다 크다면 largest_so_far의 값을 the_num으로 바꿔줍니다.
        largest_so_far = the_num
    print('largest_so_far: ', largest_so_far, 'current number: ',the_num)

print('After', largest_so_far)

# Before -1
# largest_so_far:  9 current number:  9
# largest_so_far:  41 current number:  41
# largest_so_far:  41 current number:  12
# largest_so_far:  41 current number:  3
# largest_so_far:  74 current number:  74      ## 크면 바뀌고 안크면 안바뀌고 ~ 끝까지 반복
# largest_so_far:  74 current number:  15
# After 74

#합계 구하기

zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] 
for thing in numbers :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Before 0
# 9 9
# 50 41
# 62 12
# 65 3
# 139 74
# 154 15
# After 154


#if - 아니면 elif - 도아니면 - else

#최소 찾기
smallest = None
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

# 9 9
# 9 41
# 9 12
# 3 3
# 3 74
# 3 15
# After 3