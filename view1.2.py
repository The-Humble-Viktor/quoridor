class TerminalView:
    def displayBoard(horizontal_walls, vertical_walls, p1x, p1y, p2x, p2y):

        # +--+--+
        # |  |  |
        # |     |

        columns = len(horizontal_walls[0])

        print("   ", end="")    #the row numbers on the left are 3 characters wide, so the top numbers need the same
        for c in range(columns):
            print(str(c).center(3), end="")
        print()

        for r in range(len(vertical_walls)):
            print("   ", end="")
            for c in range(columns):
                print("+--" if horizontal_walls[r][c] else "+  ",end="")
            print("+")

            print(str(r).rjust(2) + " ", end="")
            for c in range(columns):
                if p1x == r and p1y == c:
                    print("|()" if vertical_walls[r][c] else " ()",end="") #i made the arbitrary descision to represent p1 as () and p2 as []. can be changed.
                elif p2x == r and p2y == c:
                    print("|[]" if vertical_walls[r][c] else " []",end="")
                else:
                    print("|  " if vertical_walls[r][c] else "   ",end="")
            print("|") #in our case we can ignore checking again here for the last one that isnt covered because we will always have walls around the edges. 

        #last row since horizontal walls is 1 longer
        print("   ", end="")
        for c in range(columns):
            print("+--" if horizontal_walls[len(vertical_walls)][c] else "+  ", end="")
        print("+")

    def display_message(message):
        print(message)

    def get_coordinates(question):  #helper for every input that is a row and a column
        while True:
            answer = input(question).replace(",", " ").split()

            if len(answer) != 2:
                print("Please give exactly two numbers, for example: 3 4")
                continue

            try:
                x = int(answer[0])
                y = int(answer[1])
            except ValueError:
                print("Both of them have to be whole numbers, try again.")
                continue

            return (x, y)

    def get_player_action_type(player_name, walls_left):
        #while loop to get the move type (move, place hors wall, place vert wall)
        while True:
            print(player_name + ", what do you want to do? (walls left: " + str(walls_left) + ")")
            print("  1 - move your pawn")
            print("  2 - place a horizontal wall")
            print("  3 - place a vertical wall")
            print("  q - stop playing")
            choice = input("> ").strip().lower()

            if choice == "1":
                return "move"
            if choice == "2":
                return "horizontal_wall"
            if choice == "3":
                return "vertical_wall"
            if choice == "q":
                return "quit"

            print("That is not one of the options, try again.")

    def get_player_move(player_name):
        #while loop to get the coordinates for the new position
        return TerminalView.get_coordinates(player_name + ", which row and column do you want to move to? ")

    def get_player_horizontal_wall_placement(player_name):
        return TerminalView.get_coordinates(player_name + ", row and column of the horizontal wall? ")

    def get_player_vertical_wall_placement(player_name):
        return TerminalView.get_coordinates(player_name + ", row and column of the vertical wall? ")
