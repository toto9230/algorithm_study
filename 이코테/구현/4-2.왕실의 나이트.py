n = input()
row = int(n[1])
col = int(ord(n[0]) - ord('a')) + 1 #ord()는 아스키 값을 구하는 함수임.
direction = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (-1, 2), (-1, -2), (-2, 1)]

result = 0
for i in direction:
  next_x = row + i[0]
  next_y = col + i[1]
  if(next_x>=1 and next_y>=1 and next_x<=8 and next_y<=9):
    result += 1

print(result)
