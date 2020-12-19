from stack import Stack

def reverse_string(input_str):
    stack = Stack()
    for i in range(len(input_str)):
        stack.push(input_str[i])
    
    rev_string=""
    while not stack.is_empty():
        rev_string+=stack.pop()

    return rev_string


input_string = input("Enter your string: ")
print(reverse_string(input_string))
#print(input_string[::-1])