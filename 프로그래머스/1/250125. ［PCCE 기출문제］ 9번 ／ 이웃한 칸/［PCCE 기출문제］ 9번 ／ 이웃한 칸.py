def solution(board, h, w):
    count = 0
    
    n = len(board)

    dh = [0,1,-1,0]
    dw = [1,0,0,-1]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    

    return count
