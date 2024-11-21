from GUI import (Window, Point, Line )
from cell import (Cell)
from maze import Maze
def main():
    win = Window(800, 600)
    maze = Maze(50,50,5,4,120,50,win, 8)
    maze._create_cells()
    win.wait_for_close()
    """cell = Cell(win)
    cell.draw(110,110,100,100)
    cell2 = Cell(win)
    cell2.draw(500, 500, 900, 900)
    cell.draw_move(cell2)
 """


main()