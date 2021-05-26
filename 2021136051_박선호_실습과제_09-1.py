phone_dic = {'김윤섭' : '010-1234-5678', '김은솔' : '010-1234-5679', '김지수' : '010-1234-5684', '김혜연' : '010-1234-5687', '문건우' : '010-1234-5691', '박광일' : '010-1234-5693', '박상준' : '010-1234-5697', '박솔지' : '010-1234-5700', '박진현' : '010-1234-5705', '이재은' : '010-1234-5706'}

def fun_print(phone_dic):
    for temp in phone_dic.keys():
        print(temp, phone_dic[temp])

def fun_search(phone_dic,start,x):
    for k in phone_dic.keys():
        if k == start:
            print(start,"님의 전화번호는",phone_dic[start],"입니다.")
        else:
            x = x + 1
            #print(x)
    if int(len(phone_dic.keys())) == int(x):
        fun_input(phone_dic)

def fun_input(phone_dic):
    phone_dic[start] = str(input("전화번호를 입력하시오 : "))

while True:

    start = input("검색할 이름을 입력하세요 : ")

    if start == "end":
        print("전체 전화번호 목록입니다.")
        fun_print(phone_dic)
        break
    else:
        x = 0
        fun_search(phone_dic,start,x)
        fun_print(phone_dic)