#Todo - negative values to binary
from stack import Stack

def convert_dec_to_bin(decimal):
    
    if decimal == 0:
        return 0
    
    s = Stack()

    while decimal > 0:
        remainder = decimal % 2
        s.push(remainder)
        decimal = decimal // 2

    binary = ""
    while not s.is_empty():
        binary += str(s.pop())

    return binary

print(100,convert_dec_to_bin(100))
print(2,convert_dec_to_bin(2))
print(740,convert_dec_to_bin(740))
print(-244,convert_dec_to_bin(-244))

print(int(convert_dec_to_bin(5),2)==5)