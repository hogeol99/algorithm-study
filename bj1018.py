n, m = map(int,input().split())

chess_board1 = [ 
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
]
chess_board2 =  [ 
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"]
]

chess_board_input = []

for i in range(n):
    chess_board_input.append(list(input()))


a = n - 8 + 1
b = m - 8 + 1

answer = 64

for j in range(a):
    for k in range(b):
        diff1 = 0
        diff2 = 0
        for l in range(8):
            for m in range(8):
                if chess_board_input[j+l][k+m] != chess_board1[l][m]:
                    diff1 += 1
                if chess_board_input[j+l][k+m] != chess_board2[l][m]:
                    diff2 += 1
        if diff1 < answer:
            answer = diff1
        if diff2 < answer:
            answer = diff2
print(answer)

