from GUI import (Window, Point, Line )
def main():
    win = Window(800, 600)
    p1 = Point(x=0, y=0)
    p2 = Point(x=255, y=255)
    line = Line(p1,p2)
    p3 = Point(256, 255)
    p4 = Point(512, 0)
    line2 = Line(p3, p4)
    win.draw_line(line, "green")
    win.draw_line(line2, "red")
    win.wait_for_close()


main()