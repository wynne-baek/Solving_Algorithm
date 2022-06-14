A = int(input())
B = int(input())
C = int(input())
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ABC = str(A * B * C)
for num in ABC:
    count[int(num)] += 1
for i in range(10):
    print(count[i])