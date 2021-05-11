from typing import List

list = [1, 3, 2]

list.append(4)              #list에 4 추가
print("append", list)

list.sort()                 #list 정렬하기
print("sort", list)

list.reverse()              #list 반대로
print("reverse", list)

list.insert(4, 1)           #4번 위치에 1 삽입
print("insert", list)

print("len", len(list))     #list의 길이 출력

list.pop(1)                 #list에서 1번 항목 제거
print("pop", list)

list.remove(1)              #1을 제거
print("remove", list)

list2 = [5, 6]
list.extend(list2)          #list에 list2 추가
print("extend", list)

