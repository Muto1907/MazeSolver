from GUI import (Window, Point, Line )
from cell import (Cell)
def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(110,110,100,100)
    cell2 = Cell(win)
    cell2.draw(50, 50, 90, 90)
    win.wait_for_close()

main()