import turtle


class Drawable:
    def __init__(self):
        self.pointer = turtle.Turtle()
        self.screen = turtle.Screen()
        self.color = ['white', 'red', 'yellow', 'blue', 'green']

    def line_color(self, color):
        self.pointer.color(color)

    def background_color(self, color):
        self.screen.bgcolor(color)

    def Spiral(self, len):
        if len >= 5:
            self.pointer.forward(len)
            self.pointer.right(90)
            self.Spiral(len - 5)

    def Triangle(self, len):
        if len > 10:
            self.pointer.forward(len)
            self.pointer.left(120)
            self.pointer.forward(len)
            self.pointer.left(120)
            self.pointer.forward(len)

    def get_mid_point(self, x, y):
        return [ (x[0] + y[0]) / 2, (x[1] + y[1]) / 2]

    def sierpinski(self, x, y, z, level, fill):
        self.pointer.up()
        self.pointer.goto(x[0],x[1])
        self.pointer.down()
        self.pointer.fillcolor(self.color[level])
        if fill:
            self.pointer.begin_fill()
        self.pointer.goto(y[0],y[1])
        self.pointer.goto(z[0],z[1])
        self.pointer.goto(x[0], x[1])
        if fill:
            self.pointer.end_fill()
        if level:
            self.sierpinski(x, self.get_mid_point(x, y), self.get_mid_point(x, z), level - 1, True)
            self.sierpinski(y, self.get_mid_point(y, z), self.get_mid_point(y, x), level - 1, True)
            self.sierpinski(z, self.get_mid_point(z, x), self.get_mid_point(y, z), level - 1, True)
            self.sierpinski(self.get_mid_point(x,y), self.get_mid_point(y,z), self.get_mid_point(x,z), level - 1, False)

    def snowflake_full(self, level, edge):
        for i in range(3):
            self.snowflake_edge(level, edge)
            self.pointer.right(120)

    def snowflake_edge(self, level, edge):
        if level > 0:
            small_edge = edge // 3
            self.snowflake_edge(level - 1, small_edge)
            self.pointer.left(60)
            self.snowflake_edge(level - 1, small_edge)
            self.pointer.left(240)
            self.snowflake_edge(level - 1, small_edge)
            self.pointer.left(60)
            self.snowflake_edge(level - 1, small_edge)
        else:
            self.pointer.forward(edge)

    def main(self):
        self.line_color(self.color[4])
        self.background_color(self.color[0])
        self.Spiral(100)
        self.Triangle(300)
        self.sierpinski([-200,-200],[0,200], [200,-200], 2, True)
        self.snowflake_full(3, 270)
        self.screen.exitonclick()