import random
가위 = 1
바위 = 2
보 = 3
ComWin = 0
컴퓨터승수 = ComWin
HuWin = 0
사람승수 = HuWin
계속 = True

while 계속:
    컴퓨터 = random.randint(1, 3)
    사람 = int(input("가위(1), 바위(2), 보(3) 중에서 선택하세요 (끝내려면 0을 입력하세요): "))

    if 사람 == 0:
        계속 = False
        continue

    result = ""
    if 사람 == 가위:
        if 컴퓨터 == 가위:
            result = "비겼습니다!"
        elif 컴퓨터 == 바위:
            컴퓨터승수 += 1
            result = "컴퓨터가 이겼습니다!"
        else:
            사람승수 += 1
            result = "사람이 이겼습니다!"
    elif 사람 == 바위:
        if 컴퓨터 == 가위:
            사람승수 += 1
            result = "사람이 이겼습니다!"
        elif 컴퓨터 == 바위:
            result = "비겼습니다!"
        else:
            컴퓨터승수 += 1
            result = "컴퓨터가 이겼습니다!"
    elif 사람 == 보:
        if 컴퓨터 == 가위:
            컴퓨터승수 += 1
            result = "컴퓨터가 이겼습니다!"
        elif 컴퓨터 == 바위:
            사람승수 += 1
            result = "사람이 이겼습니다!"
        else:
            result = "비겼습니다!"
    else:
        print("잘못된 입력입니다. 다시 선택하세요.")
        continue

   

    if 사람승수 == 3:
        print("사람이 최종 승리하였습니다!")
        계속 = False
    elif 컴퓨터승수 == 3:
        print("컴퓨터가 최종 승리하였습니다!")
        계속 = False
