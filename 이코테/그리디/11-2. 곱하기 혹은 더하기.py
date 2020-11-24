s = input()
list_s = list(map(int, s)) #str list를 int로 바꾸고 싶을때

result = 0
for i in range(len(s)):
  if(result == 0 or list_s[i]==1):
    result += list_s[i]
  else:
    result *=list_s[i]

print(result)
