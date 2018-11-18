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

def test_misc():
    convert_decimal_to_base(25, 8)
    convert_decimal_to_base(256, 16)
    convert_decimal_to_base(26, 26)

def reverse_string_recursion(input):
    if len(input) > 1:
        input = reverse_string_recursion(input[1:]) + input[0]
    return input

def check_palimdromatic_recursion(input):
    pass