s = input()
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabet = []
number = 0
for word in s:
    if word in numbers: #반대로 알파벳인지 체크할 때는 그냥 isalpha()함수 쓰면 됨.
        number += int(word)
    else:
        alphabet.append(word)

alphabet.sort()
if number != 0:
  alphabet.append(str(number)) #숫자의 합이 0일때는 넣지 않음.
print(''.join(alphabet))  # list를 string으로 바꾸는 함수
