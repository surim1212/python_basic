a = 'hobby'
print(a.count('b'))

# 이메일 주소를 입력받습니다. 입력시 ***@** 형태입니다.
# 입력받아서 아이디만 출력해 주세요

a = "surim1212@gmail.com"
print(a[:a.find('@')])

a.strip()
a.split()

email = input('메일 주소를 입력하세요 >>> ')
print('값은 5~20',len(email))
print('값은 1이 나와야 됨',email.count('@'))
index = email.index('@')
data = email[:index]
print(data)

# 주민등록 번호를 입력받아서 다음을 출력해 줍니다.
# 성별(남자,여자)
# 생년월일(00년 2월 1일생)
# 뒤자리 숫자를 첫글자는 그대로 나머지는 *로 변경해서 출력
# 입력 시 글자 앞,뒤로 공백이 포함될수 있습니다. 공백에 대한 처리도 하세요

