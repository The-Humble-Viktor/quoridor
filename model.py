import copy

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

    def validate_move(self,x,y) -> bool:
        #compare existing pos to new, check if walls inbetween
        pass

    def validate_horizontal_wall(self,wall_coordinates: tuple) -> bool:
        new_horizontal_walls = copy.deepcopy(self.horizontal_walls)
        x, y = wall_coordinates
        new_horizontal_walls[x][y] = True
        new_horizontal_walls[x+1][y] = True

    def validate_vertical_wall(self,wall_coordinates: tuple) -> bool:
        new_vertical_walls = copy.deepcopy(self.vertical_walls)
        x, y = wall_coordinates
        new_vertical_walls[x][y] = True
        new_vertical_walls[x][y+1] = True