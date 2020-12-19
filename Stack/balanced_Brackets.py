from stack import Stack

def is_matching_brackets(p1,p2):
    return ((p1=="(" and p2==")") or (p1=="{" and p2=="}") or  (p1=="[" and p2=="]"))

def is_balanced_paren(parenthesis_string):
    s=Stack()
    is_balanced=True
    index=0
    
    while index < len(parenthesis_string) and is_balanced:
        paren = parenthesis_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced=False
            else:
                top = s.pop()
                if not is_matching_brackets(top,paren):
                    is_balanced=False
        index += 1

    if s.is_empty() and is_balanced:
        return "Balanced"
    else: return "Not Balanced"

print("String : ()(){}{} => ", is_balanced_paren("()(){}{}"))
print("String : ()){ => ", is_balanced_paren("()){"))
print("String : (({[]}))(){}{} => ", is_balanced_paren("(({[]}))(){}{}"))
print("String : ()(){}}{} => ", is_balanced_paren("()(){}}{}"))
