def convert_decimal_to_base(decimal, base):
    output = ""
    if decimal == 0:
        output = "0"
    else:
        while decimal > 0:
            remainder = decimal % base
            decimal = decimal // base
            output = "{}{}".format(remainder,output)
    print(output)

def reverse_string_recursion(input):
    if len(input) > 1:
        input = reverse_string_recursion(input[1:]) + input[0]
    return input

class Hanoi_Tower:
    def __init__(self, a):
        self.a = [i for i in range(a, 0, -1)]
        self.b = []
        self.c = []
        self.turn = 0

    def print(self):
        print("Turn {}".format(self.turn))
        print("A = {A}\nB = {B}\nC = {C}\n".format(A=self.a, B=self.b, C=self.c))
        self.turn += 1

    def execute(self, n, a, b, c):
        if n >= 1:
            self.execute(n - 1, a, c, b)
            self.print()
            c.append(a.pop())
            self.execute(n - 1, b, a, c)

    def main(self):
        self.execute(len(self.a), self.a, self.b, self.c)
        self.print()


def test_misc():
    convert_decimal_to_base(25, 8)
    convert_decimal_to_base(256, 16)
    convert_decimal_to_base(26, 26)
    Hanoi_Tower(10).main()
