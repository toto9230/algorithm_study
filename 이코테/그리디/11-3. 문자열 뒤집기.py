s = input()
group_count = 0
for i in range(len(s)):
    if (i < len(s) - 1 and s[i + 1] != s[i]):
        group_count += 1
    elif i == len(s) - 1:
        group_count += 1

if group_count % 2 == 0:  # 짝수이면
    print(group_count // 2)
elif group_count % 2 == 1:
    print(group_count // 2)
