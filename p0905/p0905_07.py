id = 'aaa'
pw = '1111'

u_id = input("아이디를 입력하세요 >> ")
u_pw = input("비밀번호를 입력하세요 >> ")

if id == u_id:
    print("아이디가 같습니다. ")
    if pw == u_pw:
        print("비밀번호가 일치합니다")
        print("로그인 되었습니다. ")
    else:
        print("비밀번호가 일치하지 않습니다. ")
else:
    print("아이디가 일치하지 않습니다. ")
# and 는 둘다 참일때 참     
if (id==u_id and pw==u_pw):
    print("아이디, 비밀번호가 일치합니다.")
    print("로그인되었습니다.")
else:
    print("아이디 또는 비밀번호가 일치하지 않습니다") 