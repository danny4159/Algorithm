def solution(board):
    max = 0
    #1. 1,1 에서 i,j 까지 탐색
    for i in range(len(board)-1):
        for j in range(len(board[1])):
            n=0
            breaker=False
            #2. 각 탐색점에서 정사각형 모양으로 점층적 탐색
            while True:
                n+=1
                #2-1. 조건1_ 탐색 가능 범위 제한  
                if i+n>len(board)-1 or j+n>len(board[1])-1:
                    break
                #2-2. 조건2_ 탐색 범위 내 모든 요소가 1이어야 정사각형
                for p in range(i,i+n):
                    for q in range(j,j+n):
                        if board[p][q] !=1:
                            breaker=True
                            break
                    if breaker==True:
                        break
                if breaker==True:
                    break
                #2-3. 조건3_ 최대값 갱신
                if (n+1)**2>max:
                    max = (n+1)**2
    return max


#board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
#board = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
board = [[0, 0, 1, 1], [1, 1, 1, 1]]
# 0	1	1	1       1
# 1	1	1	1       1
# 1	1	1	1       1
# 0	1	1	1       1
# 1     1       1       1       1

solution(board)


