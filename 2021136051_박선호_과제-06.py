#실습과제06
import math

x1, y1 = map(float,input().split(','))
x2, y2 = map(float,input().split(','))

print(x1, y1)
print(x2, y2)

result = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

print(round(result,1))