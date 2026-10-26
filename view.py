class TerminalView:
    def displayBoard(horizontal_walls, vertical_walls, p1x, p1y, p2x, p2y):

        # +--+--+
        # |  |  |
        # |     |

        columns = len(horizontal_walls[0])

        for r in range(len(vertical_walls)):
            for c in range(columns):
                print("+--" if horizontal_walls[r][c] else "+  ",end="")
            print("+")

            for c in range(columns):
                if p1x == r and p1y == c:
                    print("|()" if vertical_walls[r][c] else " ()",end="") #i made the arbitrary descision to represent p1 as () and p2 as []. can be changed.
                elif p2x == r and p2y == c:
                    print("|[]" if vertical_walls[r][c] else " []",end="")
                else:
                    print("|  " if vertical_walls[r][c] else "   ",end="")
            print("|") #in our case we can ignore checking again here for the last one that isnt covered because we will always have walls around the edges. 

        #last row since horizontal walls is 1 longer
        for c in range(columns):
            print("+",end="")
            print("--" if horizontal_walls[len(vertical_walls)][c] else "  ",end="")
        print("+")
        
    def get_player_action_type(player_name):
        #while loop to get the move type (move, place hors wall, place vert wall)
        return 

    def get_player_move(player_name):
        #while loop to get the coordinates for the new position
        return (x,y)

    def get_player_horizontal_wall_placement(player_name):
        return 

    def get_player_vertical_wall_placement(player_name):
        return    