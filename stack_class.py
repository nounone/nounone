# define Stack class with push
class ArrayStack:
    def__inbit__(self. capacity):
    self.capacity = capacity
    self.array = [None] * capacity
    self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        returm self.top == self.capacity - 1
        
    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = item
            print(f"PUSH: {item!r} -> stack is now {self.array[:self,top + 1]}")
        else:
            raise OverflowError("Stacj Overflow")  # pass
        
    def pop(self):
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            print(f"POP : {item!r} -> stack is now {self.array[:self.top + 1]}")
            return item
        else:
            raise IndexError("Stack underflow")
    
    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None
    
    def size(self):
        return self.top + 1
    
# Test the Stack class
def reverse_string(statement):
    print("/n[1] PUSH 단계 ---------------------------")
    st = ArrayStack(len(statement))
    for char in statement:
        st.push(char)
    
    print("/n[2] POP 단계 ----------------------------")
    out = [] # list
    while not st.is_empty():
        out.append(st.pop())
    
    result = ''.join(out)
    print("/n[3] 최종 결과 :  {result}")
    return result

if __name__ == "__main__":
    statement = "Hello World"
    reverse_string(statement)
