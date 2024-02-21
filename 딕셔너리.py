#리스트와 달리 딕셔너리에는 순서라는 것이 없습니다.
#대신 키(Key)라는 것이 존재합니다. 마치 물건에 포스트잇으로 라벨을 붙이는 것과 비슷합니다.
#딕셔너리는 다음과 같이 dict()라는 생성자를 통해 생성할 수 있습니다.

purse = dict() # 또는 purse = {} 와 같이 생성할 수도 있습니다.
purse['money'] = 12 # 'money'라는 키에 12라는 값 연결
purse['candy'] = 3  # 'candy'라는 키에 3이라는 값 연결
purse['tissues'] = 75 # 'tissues'라는 키에 75라는 값 연결

print(purse)
#{'money': 12, 'candy': 3, 'tissues': 75}

print(purse['candy'])
#3

purse['candy']  = purse['candy'] + 2
print(purse)
#{'money': 12, 'candy': 5, 'tissues': 75}

#딕셔너리로 이름 새기

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name in counts: 
        counts[name] = counts[name] + 1
    else :
        counts[name] = 1
print(counts)

# {'csev': 2, 'zqian': 1, 'cwen': 2}

'''
이와 같이 딕셔너리에 존재하는 키인지 아닌지 여부에 따라 처리하는 패턴은 get이라는 메소드를 사용해서 간결하게 해결할 수 있습니다.

여기에서 counts.get(name, 0)의 의미는 counts 딕셔너리에 name이라는 키가 존재할 경우 name에 대한 값을 불러오고,

그렇지 않을 경우에는 counts 딕셔너리에 name이라는 키에 0이라는 값을 갖는 데이터를 추가하라는 의미입니다.
'''

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

# {'csev': 2, 'zqian': 1, 'cwen': 2}

