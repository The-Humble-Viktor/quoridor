class Model(object):
    def __init__(self, board_height, board_width):
        self.board_height = board_height
        self.board_width = board_width


        self.horizontal_walls = [[False for _ in range(board_width)] for _ in range(board_height)]
        self.horizontal_walls[0] = [True] * (board_width)
        self.horizontal_walls.append([True] * (board_width))

        self.vertical_walls = [[False for _ in range(board_width+1)] for _ in range (board_height )]
        for row in range(board_height):
            self.vertical_walls[row][0] = True
            self.vertical_walls[row][-1] = True

        #number of players could be abstracted away, but for the sakes of gettin this done a bit quicker not right now.

        self.player1 = (0, board_width//2) 
        self.player2 = (board_height - 1, board_width // 2)

        self.walls_left = {1: 10, 2: 10} #amount of walls for each player


    def get_walls(self):
        return (self.horizontal_walls, self.vertical_walls)

    def get_p1pos(self):
        x,y = self.player1
        return x,y

    def get_p2pos(self):
        x,y = self.player2
        return x,y

    def get_walls_left(self, player_number):
        return self.walls_left[player_number]

    def on_board(self,x,y) -> bool:
        return (0 <= x < self.board_height) and (0 <= y < self.board_width)

    def wall_between(self,x,y,newx,newy) -> bool:
        if newx == x - 1:
            return self.horizontal_walls[x][y]      
        if newx == x + 1:
            return self.horizontal_walls[x+1][y]    
        if newy == y - 1:
            return self.vertical_walls[x][y]       
        return self.vertical_walls[x][y+1]        


    def validate_move(self,player_number,x,y) -> bool:
        if player_number == 1:
            currentx, currenty = self.player1
            otherx, othery = self.player2
        else:
            currentx, currenty = self.player2
            otherx, othery = self.player1

        if not self.on_board(x,y):
            return False

        if (x,y) == (otherx,othery): 
            return False

        steps = abs(x - currentx) + abs(y - currenty) 

        if steps == 1: 
            if self.wall_between(currentx,currenty,x,y):
                return False

        elif steps == 2 and (x == currentx or y == currenty): 
            middlex = (currentx + x) // 2
            middley = (currenty + y) // 2

            if (middlex,middley) != (otherx,othery): 
                return False
            if self.wall_between(currentx,currenty,middlex,middley):
                return False
            if self.wall_between(middlex,middley,x,y):
                return False

        else: 
            return False

        if player_number == 1:
            self.player1 = (x,y)
        else:
            self.player2 = (x,y)
        return True

    def validate_p1_move(self,x,y) -> bool:
        return self.validate_move(1,x,y)

    def validate_p2_move(self,x,y) -> bool:
        return self.validate_move(2,x,y)

    def pathfind(self, startX, startY, goalRow): 
        queue = [(startX,startY)]
        seen = {(startX,startY)}
        while queue:
            x, y = queue.pop()
            if x == goalRow:
                return True

            neighbors = []

            if not self.horizontal_walls[x][y]:
                neighbors.append((x-1,y))
            if not self.horizontal_walls[x+1][y]:
                neighbors.append((x+1,y))
            if not self.vertical_walls[x][y]:
                neighbors.append((x,y-1))
            if not self.vertical_walls[x][y+1]:
                neighbors.append((x,y+1))

            for cell in neighbors:
                if cell not in seen:
                    seen.add(cell)
                    queue.append(cell)

        return False

    def both_win_possible(self):
            return self.pathfind(self.player1[0],self.player1[1],self.board_height - 1) and  self.pathfind(self.player2[0], self.player2[1], 0)

    def validate_horizontal_wall(self,player_number,wall_coordinates: tuple) -> bool:
        
        x, y = wall_coordinates

        if self.walls_left[player_number] <= 0: #no walls left to place
            return False

        if not((0 < x < self.board_height) and (0 <= y < self.board_width - 1)):   
            return False

        if self.horizontal_walls[x][y] or self.horizontal_walls[x][y+1]: 
            return False
        if self.vertical_walls[x-1][y+1] and self.vertical_walls[x][y+1]: 
            return False
        
        self.horizontal_walls[x][y] = True 
        self.horizontal_walls[x][y+1] = True

        if not self.both_win_possible():
            self.horizontal_walls[x][y] = False 
            self.horizontal_walls[x][y+1] = False
            return False

        self.walls_left[player_number] -= 1
        return True

    def validate_vertical_wall(self,player_number,wall_coordinates: tuple) -> bool:
        x,y = wall_coordinates

        if self.walls_left[player_number] <= 0:
            return False

        if not ((0 <= x < self.board_height - 1) and (0 < y < self.board_width)):
            return False
        if self.vertical_walls[x][y] or self.vertical_walls[x+1][y]:
            return False
        if self.horizontal_walls[x+1][y-1] and self.horizontal_walls[x+1][y]:
            return False

        self.vertical_walls[x][y] = True
        self.vertical_walls[x+1][y] = True

        if not self.both_win_possible():
            self.vertical_walls[x][y] = False
            self.vertical_walls[x+1][y] = False
            return False

        self.walls_left[player_number] -= 1
        return True
