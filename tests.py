import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    def test_maze_create_cells_not_Squared(self):
        num_cols = 23
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 12, 8)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[1]),
            num_rows
        )

    def test_maze_entrance_and_exit(self):
        num_cols = 8
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall, False
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall, False
        )
    def test_maze_break_walls(self):
        num_cols = 8
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
    
    def test_maze_wall_reset(self):
        num_cols = 8
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()