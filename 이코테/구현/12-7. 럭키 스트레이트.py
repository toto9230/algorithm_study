n = input()
half = len(n) // 2
sum1 = 0
sum2 = 0
for i in range(half):
    sum1 += int(n[i])

for j in range(half, len(n)):
    sum2 += int(n[j])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")


#메모리: 29099kb, 시간: 76ms
