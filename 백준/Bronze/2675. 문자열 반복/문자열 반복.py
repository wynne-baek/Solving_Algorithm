T = int(input())
for _ in range(T):
    cnt, case = map(str, input().split())
    answer = ''
    for char in case:
        for __ in range(int(cnt)):
            answer += char
    print(answer)