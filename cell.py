from GUI import *
class Cell:
    def __init__(self, win=None):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2
        corner_top_left = Point(x1,y1)
        corner_top_right = Point(x2,y1)
        corner_bottom_left = Point(x1, y2)
        corner_bottom_right = Point(x2,y2)
        if self._win != None:
            if self.has_top_wall:
                top = Line(corner_top_left, corner_top_right)
                self._win.draw_line(top)
            if self.has_right_wall:
                right = Line(corner_top_right, corner_bottom_right)
                self._win.draw_line(right)
            if self.has_bottom_wall:
                bot = Line(corner_bottom_left, corner_bottom_right)
                self._win.draw_line(bot)
            if self.has_left_wall:
                left = Line(corner_top_left, corner_bottom_left)
                self._win.draw_line(left)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "grey"
        self_middle_Point = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        other_middle_Point = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        self._win.draw_line( Line(self_middle_Point, other_middle_Point), color)
        