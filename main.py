from GUI import (Window, Point, Line )
from cell import (Cell)
from maze import Maze
def main():
    win = Window(800, 600)
    maze = Maze(0,0,10,20,60,25,win)
    maze._create_cells()
    solved = maze.solve()
    if solved:
        print("The Maze is solved")
    else:
        print("The Maze couldnt be solved :(")
    win.wait_for_close()
    """cell = Cell(win)
    cell.draw(110,110,100,100)
    cell2 = Cell(win)
    cell2.draw(500, 500, 900, 900)
    cell.draw_move(cell2)
 """


main()