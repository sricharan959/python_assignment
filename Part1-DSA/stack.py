class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.top=-1

    def push(self,ele):
        self.ele=Node(ele)
        if self.head is None:
            self.head=self.ele
            self.top+=1
        else:
            last=self.head
            while(last.next):
                last=last.next
            last.next=self.ele
            self.top+=1

    
    def pop(self):
        if self.head==None:
            return 'Empty stack'
        last=self.head
        while(last.next):
            if last.next.next==None:
                popped=last.next.data
                last.next=None
                break
            last=last.next
        self.top-=1
        return popped
    
    def peek(self):
        if self.head==None:
            return 'Empty stack'
        last=self.head
        while(last.next):
            last=last.next
        return last.data
    
    def is_empty(self):
        return self.top==-1

    def display(self):
        if self.head==None:
            print(None)
            return
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

# stk=Stack()
# stk.push(2)
# stk.push(12)
# stk.push(3)
# stk.display()
# print(stk.pop())
# stk.display()