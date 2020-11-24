n = int(input())
s = list(map(int, input().split()))
s.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함되는 인원 수 
for i in s:
  count += 1
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면, 그룹결성.아니면 그냥 끝.
      result += 1
      count = 0

print(result)
