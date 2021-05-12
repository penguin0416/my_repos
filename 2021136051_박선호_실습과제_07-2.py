first = list(map(int,input("콤마로 숫자를 구분하여 입력하시오.").split(",")))
second = list(map(int,input("콤마로 숫자를 구분하여 입력하시오.").split(",")))

def add(first,second):
    list_add = [a+b for a,b in zip(first,second)]
    print("각 리스트 요소의 합 : ", list_add)

def mul(first,second):
    list_mul = [a*b for a,b in zip(first,second)]
    print("각 리스트 요소의 곱 : ", list_mul)

add(first,second)
mul(first,second)