from typing import List, Union


class SLNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SLList:

    def __init__(self, tail=None):
        self.tail = tail

    def __iter__(self):
        current = self.tail.next
        while current:
            yield current
            if current is self.tail:
                break
            current = current.next
    
    def __len__(self):
        count = 0
        node = self.tail.next
        while node:
            count += 1
            if node is self.tail:
                break
            node = node.next
        return count

    @property
    def values(self):
        return ' -> '.join([str(node.value) for node in self])

    def insertAtHead(self, data: Union[int, List[int]]):

        if isinstance(data, list):
            for v in data:
                if self.tail is None:
                    newNode = SLNode(v)
                    self.tail = newNode
                    self.tail.next = self.tail
                  
                else:
                    self.tail.next = SLNode(v, self.tail.next)
            
            return self.tail.next
        
        else:
            if self.tail is None:
                newNode = SLNode(data)
                self.tail = newNode
                self.tail.next = self.tail
            else:
                self.tail.next = SLNode(data, self.tail.next)
            
            return self.tail.next

    
def main():

    pass
    

if __name__ == "__main__":
    
    try:
        main()
    except ValueError as error:
        raise error