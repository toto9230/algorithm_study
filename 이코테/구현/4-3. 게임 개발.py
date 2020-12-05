n, m = map(int, input().split())
x, y, d = map(int, input().split())

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)] # n * m 짜리 0 배열생성
visited[x][y] = 1  # 첫 위치 1로 바꿈
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서
#1은 바다, 0 은 육지 (육지만 이동 가능)

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
        
result = 1
turn = 0
while True:
    turn_left() # step 1
    next_x = x + direction[d][0]
    next_y = y + direction[d][1]
    if game_map[next_x][next_y] == 0 and visited[next_x][next_y] == 0:
        x = next_x
        y = next_y
        visited[x][y] = 1
        result += 1
        turn = 0
    else:
        turn += 1
        if turn == 4:
            next_x = x - direction[d][0]
            next_y = y - direction[d][1]
            if game_map[next_x][next_y] == 0:  #step 3- 뒤로 갈수 있음 가기.
                x = next_x
                y = next_y
            else:
                break
            turn = 0
print(result)
