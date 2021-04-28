#저녁정하기

today_dinner = ["볶음밥", "국/찌개", "메인반찬"]

print(today_dinner)

while(11):
    print("1. 추가      2. 삭제")
    input_first = input()

    if (input_first == "1"):
        print("추가할 항목을 입력하시요.")
        today_dinner.append(input())
    elif (input_first == "2"):
        print("삭제할 항목을 입력하시오.")
        today_dinner.remove(input())
    else:
       print("잘못된 입력입니다.")
    
    print(today_dinner)

    input_second = input("1. 계속       2. 종료\n")

    if (input_second == "1"):
        continue
    elif (input_second == "2"):
        print("종료합니다.")
        break

print(today_dinner)