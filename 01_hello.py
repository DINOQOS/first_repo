def password_test():
 password = input("비밀번호를 입력하세요: ")
 while not password:
    password = input("다시 비밀번호를 입력하세요: ")
 return password

returned = password_test()
