s = input()
numbers = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9']

alphabet = []
number = 0
for word in s:
  if word in numbers:
    number += int(word)
  else:
    alphabet.append(word)

alphabet.sort()
alphabet.append(str(number))
print(''.join(alphabet)) # list를 string으로 바꾸는 함수 
