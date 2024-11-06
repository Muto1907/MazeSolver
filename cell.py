from GUI import *
class Cell:
    def __init__(self, win):
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
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        corner_top_left = Point(x1,y1)
        corner_top_right = Point(x2,y1)
        corner_bottom_left = Point(x1, y2)
        corner_bottom_right = Point(x2,y2)
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

