from view import TerminalView as View
from model import Model as Game

def main():
    test()


def test():
    game = Game(5,8)
    h, v = game.get_walls()
    p1x, p1y = game.get_p1pos()
    p2x, p2y = game.get_p2pos()
    View.displayBoard(h, v,p1x,p1y, p2x,p2y)
    print(game.validate_horizontal_wall((4,0)))
    print(game.validate_horizontal_wall((4,2)))
    print(game.validate_horizontal_wall((4,4)))   
    print(game.validate_horizontal_wall((3,6)))   #change x to 4, and see that validate_horizontal_wall becomes false
    View.displayBoard(h, v,p1x,p1y, p2x,p2y)
    print("Both players win possible: "+str(game.both_win_possible()))

if __name__ == "__main__":
    main()