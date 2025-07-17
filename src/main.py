import util as util

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

util.display_board(board)
playing = True

while playing:
    board = util.enter_move(board)
    if util.victory_for(board, 'O'):
        playing = False
    else:
        board = util.draw_move(board)
        if util.victory_for(board, 'X'):
            playing = False

