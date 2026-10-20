
class Model(object):
    def __init__(self, board_height, board_width):
        self.horizontal_walls = [[False for _ in range(board_width - 1)] for _ in range(board_height)]
        self.horizontal_walls[0] = [True] * (board_width - 1)
        self.horizontal_walls[-1] = [True] * (board_width - 1)

        self.vertical_walls = [[False for _ in range(board_width)] for _ in range (board_height - 1)]
        for row in range(board_height - 1):
            self.vertical_walls[row][0] = True
            self.vertical_walls[row][-1] = True

        player1 = (0, board_width//2)
        player2 = (board_height - 1, board_width // 2)


    def get_walls(self):
        return (self.horizontal_walls, self.vertical_walls)

    def validate_move(x,y) -> bool:
        #compare existing pos to new, check if walls inbetween
        pass

    def validate_horizontal_wall(new_horizontal_walls) -> bool:
        pass

    def validate_vertical_wall(new_vertical_walls) -> bool:
        pass