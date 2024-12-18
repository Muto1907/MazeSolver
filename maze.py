from cell import Cell
import time, random
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
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.seed = seed
        if self.seed != None:
            random.seed(self.seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
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
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        if self._num_cols > 0 and self._num_rows > 0:
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0,0)
            self._cells[self._num_cols-1] [self._num_rows-1].has_bottom_wall = False
            self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self,i ,j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if self._num_cols > 1 + i:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))
            if 0 <= i - 1:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))
            if self._num_rows > 1 + j:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))
            if 0 <= j - 1:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction_index = random.randrange(len(to_visit))
            direction = to_visit[direction_index]
            if direction[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            elif direction[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if direction[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            elif direction[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols -1 and j == self._num_rows -1:
            return True
        #i - 1 left
        if i - 1 >= 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            is_finished = self._solve_r(i-1, j)
            if is_finished:
                return is_finished
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        #i + 1 right
        if i + 1 < self._num_cols and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            is_finished = self._solve_r(i+1, j)
            if is_finished:
                return is_finished
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        #j - 1 top
        if j - 1 >= 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            is_finished = self._solve_r(i, j-1)
            if is_finished:
                return is_finished
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
    	#j + 1 bottom
        if j + 1 < self._num_rows and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            is_finished = self._solve_r(i, j+1)
            if is_finished:
                return is_finished
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        return False