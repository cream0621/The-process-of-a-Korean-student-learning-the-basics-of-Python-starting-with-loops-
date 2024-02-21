'''
문자열에 split 메소드를 실행시키면 다음과 같이 띄어쓰기를 기준으로 문장을 분할해 단어들의 리스트로 만들어줍니다.
(참고로, 별도의 옵션을 사용하면 공백 문자(스페이스바)가 아닌 다른 문자를 기준으로도 분할할 수 있습니다)
'''

line = 'The general pattern to count the words'
print(line.split())

# ['The', 'general', 'pattern', 'to', 'count', 'the', 'words']

counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

# chuck 1
# fred 42
# jan 100

'''keys, values 메소드로는 딕셔너리의 키와 값의 쌍을 얻을 수 없었는데요, 키와 값의 쌍을 얻기 위해서는 items 메소드를 사용하면 됩니다.
다음과 같이 딕셔너리에 items 메소드를 실행하면 '튜플(tuple)'이라는 자료 구조 안에 키와 값이 쌍을 이루어 저장된 리스트가 반환됩니다.
(튜플에 대해서는 다음 단원에 배우겠습니다)'''

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(jjj.items())
# [('jan', 100), ('chuck', 1), ('fred', 42)]

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for aaa,bbb in jjj.items() :
    print(aaa, bbb)

# chuck 1
# fred 42
# jan 100
    
