n = int(input())
datas = input().split()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
direction = ['R', 'L', 'D', 'U']
x, y = 1, 1

for data in datas:
    for i in range(len(direction)):
      if (data == direction[i]):
         next_dx = x + dx[i]
         next_dy = y + dy[i]
    if 1<=next_dx<=n and 1<=next_dy<=n :
      x = next_dx
      y = next_dy

print(x, y)
