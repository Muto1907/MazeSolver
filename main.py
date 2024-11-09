from GUI import (Window, Point, Line )
from cell import (Cell)
def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(110,110,100,100)
    cell2 = Cell(win)
    cell2.draw(500, 500, 900, 900)
    cell.draw_move(cell2)
    win.wait_for_close()

main()