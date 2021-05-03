#실습과제06
import math                                                                #수학함수 불러오기

def fun_distance():                                                        #함수 fun_distance 생성
    x1, y1 = map(float,input("첫번째 좌표를 입력하시오.").split(','))        #지역변수 x1,y1
    x2, y2 = map(float,input("두번째 좌표를 입력하시오.").split(','))        #지역변수 x2,y2

    print("첫번째 좌표는 (",round(x1,1), round(y1,1),") 이다.")
    print("두번째 좌표는 (",round(x2,1), round(y2,1),") 이다.")

    result = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))                        #좌표 사이 거리 구하기

    print("두 좌표 사이의 거리는", round(result,1), "이다.")                 #학번이 1로 끝나므로 소숫점 자리수 1
    
fun_distance()