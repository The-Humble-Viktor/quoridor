from view_2 import TerminalView as View
from model_2 import Model as Game

def main():
    game = Game(5,8)
    try:
        play(game)
    except (KeyboardInterrupt, EOFError):  #ctrl+c or no input left
        View.display_message("")
        View.display_message("Game stopped.")


def play(game):
    players = [("Player 1", 1), ("Player 2", 2)]
    turn = 0

    while True:
        show_board(game)
        player_name, player_number = players[turn % 2]

        if not take_turn(game, player_name, player_number): #the player chose to stop
            View.display_message("Game stopped.")
            return

        if has_won(game, player_number):
            show_board(game)
            View.display_message(player_name + " wins!")
            return

        turn += 1


def take_turn(game, player_name, player_number): #keep asking until the model accepts, gives back False if the player stops
    while True:
        action = View.get_player_action_type(player_name, game.get_walls_left(player_number))

        if action == "quit":
            return False

        if action == "move":
            x, y = View.get_player_move(player_name)
            if player_number == 1:
                accepted = game.validate_p1_move(x,y)
            else:
                accepted = game.validate_p2_move(x,y)
        elif action == "horizontal_wall":
            accepted = game.validate_horizontal_wall(player_number, View.get_player_horizontal_wall_placement(player_name))
        else:
            accepted = game.validate_vertical_wall(player_number, View.get_player_vertical_wall_placement(player_name))

        if accepted:
            return True

        if action == "move":
            View.display_message("You can only step to one cell next to you (not diagonally) if no wall is in the way,")
            View.display_message("or jump straight over the other pawn. Try again.")
        else:
            View.display_message("A wall has to fit in an empty spot on the board, it cannot cross another wall and it")
            View.display_message("cannot close a player off completely. You also need to have walls left. Try again.")


def has_won(game, player_number): #p1 starts at the top and has to reach the bottom row, p2 the other way around
    if player_number == 1:
        x, y = game.get_p1pos()
        return x == game.board_height - 1

    x, y = game.get_p2pos()
    return x == 0


def show_board(game):
    h, v = game.get_walls()
    p1x, p1y = game.get_p1pos()
    p2x, p2y = game.get_p2pos()
    View.displayBoard(h, v,p1x,p1y, p2x,p2y)


def test():
    game = Game(5,8)
    h, v = game.get_walls()
    p1x, p1y = game.get_p1pos()
    p2x, p2y = game.get_p2pos()
    View.displayBoard(h, v,p1x,p1y, p2x,p2y)
    print(game.validate_horizontal_wall(1,(4,0)))
    print(game.validate_horizontal_wall(1,(4,2)))
    print(game.validate_horizontal_wall(1,(4,4)))   
    print(game.validate_horizontal_wall(1,(3,6)))   #change x to 4, and see that validate_horizontal_wall becomes false
    View.displayBoard(h, v,p1x,p1y, p2x,p2y)
    print("Both players win possible: "+str(game.both_win_possible()))

if __name__ == "__main__":
    main()
