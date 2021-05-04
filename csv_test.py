#csv_test
#알고리즘 : 저장된 파일 불러오기 - 파일을 리스트에 입력 - 리스트 수정 - 리스트를 다시 파일에 입력 -> while문으로 반복

import csv

example = []

#File_Read
with open('example.txt', 'r') as text_file:
    example_list = []
    line = text_file.readline()

    while line !='':
        example_list.append(line)
        line = text_file.readline()

while(11):
    print("1. 추가      2. 삭제")
    input_first = input()

    if (input_first == "1"):
        print("추가할 항목을 입력하시요.")
        example.append(input())
    elif (input_first == "2"):
        print("삭제할 항목을 입력하시오.")
        example.remove(input())
    else:
       print("잘못된 입력입니다.")

    print(example)

    input_second = input("1. 계속       2. 종료\n")

    if (input_second == "1"):
        continue
    elif (input_second == "2"):
        print("종료합니다.")
        break

#File_Write
with open('example.txt', 'w') as f:
    for line in example:
        f.write(line)
    
