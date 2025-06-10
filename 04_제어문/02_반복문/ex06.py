# 가위바위보 게임 
# : 컴퓨터랑 가위바위보 게임을 하여, 질 때까지 반복하는 게임을 완성하시오. 



import random
choices = ["가위", "바위", "보"]

# random.choice( 리스트 ) :  리스트 요소 중 하나를 랜덤으로 선택 
computer = random.choice(choices)

win = True

while win:
    computer = random.choice(choices)
    person = input("가위 바위 보 중 하나를 입력하시오.")
    print('컴퓨터 : {}'.format(computer))
    print('사람 : {}'.format(person))
    
    win1 = (person == "가위" and computer == "보")
    win2 = (person == "바위" and computer == "가위")
    win3 = (person == "보" and computer == "바위")
    
    if person == computer:
        win = True
        print("비겼습니다!")    
    elif win1 or win2 or win3:
        win = True
        print("이겼습니다!")
    else:
        win = False
        print("졌습니다!")


    



