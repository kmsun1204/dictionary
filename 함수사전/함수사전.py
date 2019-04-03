# 1. 학번 입학년도
#실행결과 :studentnumber()
# 학번: >? 201910284
# 학번: 19 입학년도: 2019
def studentnumber():
    a=input("학번: ")
    b=a[2:4]
    c=a[:4]
    print("학번: %s" %b , "입학년도: %s" %c)

# 2. 김민선이 싫어하는음식
# 실행결과 :hatefood()
# 김민선이 싫어하는 음식은? :  >? 스테이크
# 땡
def hatefood():
    a= input("김민선이 싫어하는 음식은? :  ")
    b = "해파리냉채"
    if a == b :
      print("딩동댕")
    else:
      print("땡")

#3. 호그와트 기숙사 테스트
# 실행결과:hogwartsdormitorytest()
# 자신의 가장 큰 가치관은? : >? 돈
# 머글입니다.
def hogwartsdormitorytest():
    a = input("자신의 가장 큰 가치관은? : ")
    b= ("용기" or "기사도")
    c = ("지혜" or "지식" or "배움")
    d = ("야망" or "혈통")
    e = ("성실" or "화합")
    if a == b:
       print("그리핀도르")
    elif a == c:
       print("레번클로")
    elif a == d:
       print("슬리데린")
    elif a == e:
       print("후푸푸푸")
    else:
       print("머글입니다.")

# 4. 이상
#실행결과:kid()
#제 1 아이가무섭다그리오.
#제 2 아이가무섭다그리오.
#제 3 아이가무섭다그리오.
#제 4 아이가무섭다그리오.
#제 5 아이가무섭다그리오.
#제 6 아이가무섭다그리오.
#제 7 아이가무섭다그리오.
#제 8 아이가무섭다그리오.
#제 9 아이가무섭다그리오.
#제 10 아이가무섭다그리오.
#제 11 아이가무섭다그리오.
#제 12 아이가무섭다그리오.
#제 13 아이가무섭다그리오.
#제 13 인의아이는무서운아이와무서워하는아이와그렇게뿐이모였오.
def kid():
    kid=0
    while kid < 13:
        kid = kid +1
        print("제 %d 아이가무섭다그리오." % kid)
        if kid == 13:
            print("제 13 인의아이는무서운아이와무서워하는아이와그렇게뿐이모였오.")

# 5. 위락식상메뉴정하기
#실행결과 menu()
#가지고있는 돈 (원) : >? 6000
#순두부 or 제육볶음
def menu():
    a = int(input("가지고있는 돈 (원) : "))
    if 5000> a >= 4000:
        print("라볶이 or 알밥")
    elif 6500> a >= 5000:
        print("순두부 or 제육볶음")
    elif a >= 6500:
        print("김치치즈덮밥 or 오징어덮밥")
    else :
        print("죄송하지만 위락식당에선 메뉴를 고르실 수 없습니다.")


# 6. 이런 시
# 실행결과 : poem()
# 내가 그다지 사랑하던 그대여
# 내 한 평생에 차마 그대를 잊을 수 없소이다.
# 내 차례에 못 올 사람인 줄은 알면서도
# 나 혼자는 내내 생각하리라.
# 자, 그러면
# 내내 어여쁘소서
def poem():
    text_list = ["내가 그다지 사랑하던 그대여","내 한 평생에 차마 그대를 잊을 수 없소이다.","내 차례에 못 올 사람인 줄은 알면서도","나 혼자는 내내 생각하리라.","자, 그러면","내내 어여쁘소서"]
    for i in text_list:
        print(i)

# 7. 단어놀이
# 실행결과: word()
# 옷,양말,호수엔 어떤 색이 어울릴까요? : >? d
# 빨간옷
# 노란양말
# 푸른호수
def word():
    input("옷,양말,호수엔 어떤 색이 어울릴까요? : ")
    a = [("빨간","옷"), ("노란","양말"),("푸른","호수")]
    for (first, last) in a:
        print(first + last)


# 8. 어떤외투를입을까
# 실행결과:clothes()
# 오늘 기온은 몇 도인가요?(숫자만): >? 3
# 패딩
def clothes():
    a= int(input("오늘 기온은 몇 도인가요?(숫자만): "))
    if a >= 16 :
        print("외투 안 입어도됨")
    elif 16> a >=11 :
        print("트렌치코트 or 자켓")
    elif 11> a >= 6 :
        print("코트")
    elif 5 >= a > -1 :
        print("패딩")
    else:
        print("나가지마세요")


# 9. 구구단
# 실행결과:nineninedan()
# 2 4 6 8 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81
def nineninedan():
    for i in range(2,10):
        print("")
        for j in range(1,10):
          print(i * j, end=" ")


# 10. 나눗셈 몫
# 실행결과:partofdivision(3,10)
# 3
def partofdivision(a,b):
    print(b//a)


# 11. 나눗셈 나머지
# 실행결과:remainder(2,11)
# 1
def remainder(a,b):
    print(b%a)


#12. 나눗셈
# 실행결과:division(3,9)
# 3.0
def division(a,b):
    print(b/a)


#13. 가장 좋아하는 음식
# 실행결과:lovefood()
# my favorite foodissteak
def lovefood():
    a=("steak")
    b=("my favorite food")
    print(b+ "is" + a)

#14. 가시리가시리
# 실행결과:go()
# 가시리가시리 잇고 나난
def go():
    a="가시리"
    b="잇고"
    c="나난"
    print(a*2 , b , c)


#15. 더하기
# 실행결과:add(3,9)
# 12
def add(a,b):
    print(a+b)


#16. 빼기
# 실행결과:minus(7,5)
# 2
def minus(a,b):
    print(a-b)

#17. 곱하기
# 실행결과:multiply(8,4)
# 32
def multiply(a,b):
    print(a*b)


#18. 세금 뗀 후 알바비
# 실행결과:allowance()
# 시급을 쓰시오: (원)>? 10000
# 일한 시간을 쓰시오(초과수당 계산 안 됨): (시간)>? 34
# 32878000.0
def allowance():
    a=int(input("시급을 쓰시오: (원)"))
    b=int(input("일한 시간을 쓰시오(초과수당 계산 안 됨): (시간)"))
    c= (a*b*96.7)
    print(c)


#19. 식재료 개수 편하게 볼 수 있는 법
# 실행결과:countfood()
# 계란은 몇 알 남았나요?: (개)>? 3
# 돼지고기는 몇 근 남았나요?: (개)>? 4
# 양파는 몇 알 남았나요?: (개)>? 2
# 계란은 3알 있습니다. 돼지고기는 4 근 있습니다. 양파는 2 알 있습니다. 재료가 충분하다면 볶음밥 어떠세요?
def countfood():
    a=int(input("계란은 몇 알 남았나요?: (개)"))
    b=int(input("돼지고기는 몇 근 남았나요?: (개)"))
    c=int(input("양파는 몇 알 남았나요?: (개)"))
    print("계란은 %d알 있습니다." %a ,"돼지고기는 %d 근 있습니다."%b , "양파는 %d 알 있습니다."%c ,"재료가 충분하다면 볶음밥 어떠세요?" )


#20. 마카롱추천
# 실행결과:macaron()
# 마카롱 필링이 많은 걸 원하시나요?:  (yes/no)>? yes
# 꼬끄는 바삭한 걸 좋아하시나요?: (yes/no)>? yes
# 나비부엌을 추천해요!
def macaron():
    a=input("마카롱 필링이 많은 걸 원하시나요?:  (yes/no)")
    b=input("꼬끄는 바삭한 걸 좋아하시나요?: (yes/no)")
    if   a== "yes" and b=="yes":
           print("나비부엌을 추천해요!")
    elif a== "yes" and b=="no":
           print("나이스 미팅 유를 추천해요!")
    elif a=="no" and b=="yes" :
           print("라듀레를 추천해요!")
    else:
           print("파리바게트를 추천해요!")

#21. 수익- 지출
# 실행결과:money()
# 이번 달 수익은?: (원)>? 300000
# 이번 달 지출은?: (원)>? 100000
# 남은 돈은 : 200000
def money():
    a= int(input("이번 달 수익은?: (원)"))
    b= int(input("이번 달 지출은?: (원)"))
    print( "남은 돈은 :",a-b)

#22. 목표와 실제
# 실행결과:moneyplan()
# 목표 저금 액: (원)>? 200000
# 실제 저금 액: (원)>? 1000
# 커다란 실패..
def moneyplan():
    a= int(input("목표 저금 액: (원)"))
    b= int(input("실제 저금 액: (원)"))
    if b >=a :
        print("수고했어요! *목표달성*")
    else:
        print("커다란 실패..")

#23. 가우스 일화(1~100까지 더하는 법)
# 실행결과:gauss()
# 5050
def gauss():
    sum = 0
    for i in range(1,101):
     sum = sum+i
    print (sum)

#24. 내가 넣은 숫자안에 속한 짝수만 출력하기
# 실행결과:even()
# 원하는 수를 넣으시오 : >? 10
# 2
# 4
# 6
# 8
# 10
def even():
    c = int(input("원하는 수를 넣으시오 : "))
    a = 0
    while a < c:
        a = a + 1
        if a % 2 == 1:continue
        print(a)

#25. 내가 넣은 숫자안에 속한 홀수만 출력하기
# 실행결과:odd()
# 원하는 수를 넣으시오: >? 7
# 1
# 3
# 5
# 7
def odd():
    c = int(input("원하는 수를 넣으시오: "))
    a = 0
    while a <= c - 1:
        a=  a + 1
        if a % 2 == 0:continue
        print(a)

#26. 마스크를 껴야할까?
# 실행결과:mask()
# 미세먼지 지수는?(숫자로 쓰시오): >? 30
# 마스크를 안껴도 괜찮아요!
def mask():
    a=int(input ("미세먼지 지수는?(숫자로 쓰시오): ") )
    if 80>= a :
        print("마스크를 안껴도 괜찮아요!")
    elif 150 >= a >= 81 :
        print("마스크 끼세요!")
    else :
        print("나가지 마세요")

#27. 개인정보
# 실행결과:information()
# {'이름': '김민선', '혈액형': 'B', '통학방법': '지하철'}
def information():
    i = {"이름":"김민선", "혈액형" :"B", "통학방법": "지하철"}
    print(i)

#28.더치페이, 반올림함
# 실행결과:dutchpay()
# 사람 수를 입력하세요: (명)>? 3
# 총 금액을 입력하세요: (원)>? 10000
# 3333
def dutchpay():
    people= int(input("사람 수를 입력하세요: (명)"))
    money= int(input("총 금액을 입력하세요: (원)"))
    a= money/people
    print(round (a))

#29.삼각형 넓이 구하는 법
# 실행결과:triangle()
# 높이 : >? 2
# 밑변 : >? 4
# 4.0
def triangle():
    a=int(input("높이 : "))
    b=int(input("밑변 : "))
    print(a*b/2)


#30.cm 를 m로 바꾸기
# 실행결과:cm()
# m로 단위를 바꾸고 싶은 cm의 값: (cm)>? 30
# 0.3 m 이다.
def cm() :
    a=int(input("m로 단위를 바꾸고 싶은 cm의 값: (cm)"))
    b= a * 0.01
    print("%s m 이다." %b)


#31.m를 km로 바꾸기
# 실행결과:m()
# km로 단위를 바꾸고 싶은 m의 값: (m)>? 3000
# 3.0 km이다.
def m() :
    a=int(input("km로 단위를 바꾸고 싶은 m의 값: (m)"))
    b= a * 0.001
    print("%s km이다."%b)

