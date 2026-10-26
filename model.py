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


    def get_walls(self):
        return (self.horizontal_walls, self.vertical_walls)

    def get_p1pos(self):
        x,y = self.player1
        return x,y

    def get_p2pos(self):
        x,y = self.player2
        return x,y
        
    def validate_p1_move(self,x,y) -> bool:  #number of players could be abstracted away
        currentx, currenty = self.player1

        if currentx == x:
            if abs(y - currenty) != 1 or y < 0 or y >= self.board_width:
                return False
        elif currenty == y:
            if abs(x - currentx) != 1 or x < 0 or x > self.board_height:
                return False
        self.player1 = (x,y)
        return True

    def validate_p2_move(self,x,y) -> bool:
        currentx, currenty = self.player2

        if currentx == x:
            if abs(y - currenty) != 1 or y < 0 or y >= self.board_width:
                return False
        elif currenty == y:
            if abs(x - currentx) != 1 or x < 0 or x >= self.board_height:
                return False
        self.player2 = (x,y)
        return True

    def pathfind(self, startX, startY, goalRow): #check if we can ever reach a cell with y = goalY starting at startX,startY
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

    def validate_horizontal_wall(self,wall_coordinates: tuple) -> bool:
        
        x, y = wall_coordinates

        if not((0 < x < self.board_height) and (0 <= y < self.board_width - 1)):   #make sure x and y are bounded to the possible placement values
            return False

        if self.horizontal_walls[x][y] or self.horizontal_walls[x][y+1]: #already some horizontal wall placed on either of them
            return False

        if self.vertical_walls[x-1][y+1] and self.vertical_walls[x][y+1]: #equivalent vertical wall crossing the horizontal wall
            return False
        
        self.horizontal_walls[x][y] = True #doing and then undoing two booleans is much more efficient in this case
        self.horizontal_walls[x][y+1] = True

        if not self.both_win_possible():
            self.horizontal_walls[x][y] = False #undo!
            self.horizontal_walls[x][y+1] = False
            return False

        return True

    def validate_vertical_wall(self,wall_coordinates: tuple) -> bool:
        #TODO mirror what is done in validate_horizontal_wall()...
        pass