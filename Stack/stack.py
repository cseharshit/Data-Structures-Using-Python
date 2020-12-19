class Stack():
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
    

if __name__ == "__main__":
    stackA = Stack()
    stackA.push(1)
    stackA.push(2)
    stackA.push(3)
    stackA.push(4)
    print("\nStack - ", stackA.get_stack())
    print(stackA.pop())
    print(stackA.pop())
    print(stackA.pop())
    print("Is Stack Empty - ", stackA.is_empty())
    print("Top Element - " , stackA.peek())
    print(stackA.pop())
    print("Is Stack Empty - ", stackA.is_empty())
    print("\nStack - ", stackA.get_stack())