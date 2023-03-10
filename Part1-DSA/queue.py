class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue():
    def __init__(self):
        self.head=None
        self.front=0
        self.rear=-1
    
    def enqueue(self,ele):
        self.ele=Node(ele)
        if self.head is None:
            self.head=self.ele
            self.rear+=1
        else:
            self.ele.next=self.head
            self.head=self.ele
            self.rear+=1

    def dequeue(self):
        if self.head is None:
            return "Empty"
        last=self.head
        while(last.next):
            if last.next.next==None:
                de=last.next.data
                last.next=None
                break
            last=last.next
        self.front+=1
        return de
    
    def peek(self):
        if self.head==None:
            return 'Empty Queue'
        last=self.head
        return last.data
    
    def is_empty(self):
        return self.rear==-1

# q=Queue()
# print(q.is_empty())
# q.enqueue(2)
# q.enqueue(13)
# q.enqueue(4)
# q.enqueue(41)
# print(q.dequeue())
# print(q.peek())