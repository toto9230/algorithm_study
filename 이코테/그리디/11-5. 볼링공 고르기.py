
n, m = map(int, input().split())
k = list(map(int, input().split()))

combination = int((n*(n-1))/2) # combination(n, 2)로 해도 됨. 
#중복 갯수 찾기
count = []
for i in range(1,m+1):
  cnt = 0
  for j in k:
    if i ==j:
      cnt +=1
  count.append(cnt)

minus_count = 0
for i in count:
  minus_count += (i//2)

print(combination - minus_count)
