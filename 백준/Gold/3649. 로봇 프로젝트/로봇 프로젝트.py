import sys

"""
구멍의 너비 X(센티미터)
레고 조각 수 N
레고 길이 L개(나노미터)
1) 입력받기(최소힙, 최대힙)
-> 입력 받고, 정렬
2) 투포인터 설정해 더하면서 계산하기
"""

while True:
    try:
        X = int(input()) * 10000000
        N = int(input())
        piece = [int(input()) for _ in range(N)]
        piece.sort()
    # print(piece)
        start, end = 0, N-1
        flag = True
        while start < end:
            if piece[start] + piece[end] == X:
                print(f'yes {piece[start]} {piece[end]}')
                flag = False
                break
            elif piece[start] + piece[end] < X:
                start += 1
            elif piece[start] + piece[end] > X:
                end -= 1
        if flag:
            print('danger')
    except:
        break