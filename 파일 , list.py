fhand = open('hello.txt', 'r') #open() : 파일을 여는 내장함수

# open('파일명입력', '모드 선택')
# 1. 파일명 입력
# 파일명은 문자열 타입으로 입력하며, 확장자까지 포함시켜 줍니다.
# 2. 모드 선택
# 모드에서는 w 또는 r 두가지를 선택할 수 있습니다. 'w'는 파일을 작성할 때 사용하며, 'r'은 파일을 읽을 때 사용합니다.

# \n  : 줄바꾸기 (개행문자0)


#list :[여기에, 이렇게, 끼워넣는거임]

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']
colors = ['red', ['yellow','blue'], 'black']
emptyList = []
print(colors[0])
# red라고 출력됨
lotto = [2, 14, 26, 41, 63]
print(lotto)
# [2, 14, 26, 41, 63]이 출력됨
lotto[2] = 28
print(lotto)
# [2, 14, 28, 41, 63]이 출력됨

friends = ['Joseph', ' Glenn', 'Sally']
print(len(friends))  #len() : 원소의 개수?
# 3으로 출력됨

for i in range(2, 8): #range() 범위?
    print(i) 

# 2부터 7까지의 수
    
#----------------------------
    
#list 연산
    
#합
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
# [1, 2, 3, 4, 5, 6]로 출력됩니다.

#슬라이싱
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# [41, 12]
# [9, 41, 12, 3]
# [3, 74, 15]
# [9, 41, 12, 3, 74, 15] 로 출력됩니다.

friends = list()
friends.append('Joseph')
friends.append('Glenn')
friends.append('Sally')
print(friends)
# ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
# ['Glenn', 'Joseph', 'Sally']
print('Glenn' in friends)
# True로 출력됩니다.

'''
friends = list(): 비어있는 리스트를 생성합니다.
friends.append('Joseph'): 'Joseph'라는 이름을 리스트에 추가합니다. #append : 요소추가 (. 은 객체에 속성에 접근하는 연산자)
friends.append('Glenn'): 'Glenn'이라는 이름을 리스트에 추가합니다.
friends.append('Sally'): 'Sally'라는 이름을 리스트에 추가합니다.
print(friends): 현재 리스트의 내용을 출력합니다. 결과로 ['Joseph', 'Glenn', 'Sally']가 출력됩니다.
friends.sort(): 리스트의 요소들을 알파벳 순서로 정렬합니다.
print(friends): 정렬된 리스트의 내용을 출력합니다. 결과로 ['Glenn', 'Joseph', 'Sally']가 출력됩니다.
'Glenn' in friends: 'Glenn'이 리스트에 있는지 확인합니다. 결과로 True가 출력됩니다.
'''


#활용 : 이메일 주소 추출

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# line 에 uct.ac.za만 추출하는 방법을 찾아 보도록 하겠습니다.
words = line.split()
# words는 해당 라인을 빈칸을 구분자로 하여 리스트로 저장됩니다.
print(words[1])
# stephen.marquard@uct.ac.za이 출력됩니다.
email = words[1]
address = email.split('@')
print(address)
# ['stephen.marquard', 'uct.ac.za'] 가 출력됩니다.
print(address[1])
# uct.ac.za가 출력됩니다.



