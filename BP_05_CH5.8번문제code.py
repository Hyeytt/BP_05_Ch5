import turtle                    #turtle 함수를 불러온다                      

t = turtle.Turtle()             # 변수 t를 turtle함수와 같다고 정함

t.shape("turtle")               # t를 거북이 모양으로 정함

x1 : int(input("큰 원의 중심좌표 x1:"))   # x1값을 input함수를 사용해 입력받는다
y1 : int(input("큰 원의 중심좌표 y1:"))   # y1값을 input함수를 사용해 입력받는다
r1 : int(input("큰 원의 반지름 :"))       # r1값을 input함수를 사용해 입력받는다
x2 : int(input("작은 원의 중심좌표 x2:")) # x2값을 input함수를 사용해 입력받는다
y2 : int(input("작은 원의 중심좌표 y2:")) # y1값을 input함수를 사용해 입력받는다
r2 : int(input("작은 원의 반지름 r2:"))   # r2값을 input함수를 사용해 입력받는다

t.penup()                                # 펜을 든다
t.goto(x1, y1)                           # goto함수를 이용해 좌표 x1,y1로 이동시킨다
t.pendown()                              # 펜을 내린다
t.circle(r1)                             # r1만큼의 반지름을 가진 원을 가짐

t.penup()                                # 펜을 든다
t.goto(x2, y2)                           # goto함수를 이용해 좌표 x2,y2로 이동시킨다 
t.pendown()                              # 펜을 내린다
t.circle(r2)                             # r2만큼의 반지름을 가진 원을 가짐

dist = ((x1- x2) * (x1-x2) + (y1 - y2) * (y1 -y2)) ** 0.5  # 점과 점 사이를 구하는 공식이다
if dist <= r1-r2 :                       # 반지름의 차이를 원의 중심사이의 거리와 비교한다.
    turtle.write("두번째 원이 첫번째 원의 내부에 있습니다.") #write 함수를 사용한다.
elif dist <= r1 + r2:                    # 반지름의 차이를 원의 중심사이의 거리와 비교한다.
    turtle.write("두번째 원이 첫번째 원과 겹칩니다.")
else:
    turtle.write("두번째 원이 첫번째 원과 겹치지 않습니다.") 

t._screen.exitonclick()  #클릭을 해야 종료가 되게 만드는 함수
