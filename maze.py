from cell import Cell
import time
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range (self._num_rows):
                self._cells[i].append(Cell(self._win))
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        position_x1 = self._cell_size_x * i + self._x1
        position_x2 = self._cell_size_x * (i+1) + self._x1
        position_y1 = self._cell_size_y * j + self._y1
        position_y2 = self._cell_size_y * (j + 1) + self._y1
        self._cells[i][j].draw(position_x1, position_y1, position_x2, position_y2)
        self._animate()
    
    def _animate(self):
        if not self._win:
            return
        self._win.redraw
        time.sleep(0.05)