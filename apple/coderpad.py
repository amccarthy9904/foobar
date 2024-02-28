


# lru cache
# basic data structs
# add O(1) retrieve O(1)
# 10 items max
# least recently used item must be kicked out

class Node:
    def __init__(self, val, key) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
    def get_next(self):
        return self.next
    
    def remove_last(self):
        self.prev.prev.next = self.end

class LRU:

    def __init__(self) -> None:
        self.dict = {}
        self.head = Node(None, None)
        self.end = Node(None, None)
        self.head.next = self.end

    def add(self, k, v):

        if k in self.dict:

            if self.head.next.key == k:
                self.head.next.val = v
            else:
                old_node = self.dict[k]
                self.head.next.prev = old_node
                old_node.next = self.head.next
                self.head.next = old_node
                old_node.prev = self.head
                old_node.val = v

        else:
            new_node = Node(v, k)
            self.dict[k] = new_node
            self.head.next.prev = new_node
            new_node.next = self.head.next
            self.head.next = new_node
            new_node.prev = self.head

            if len(self.dict.keys()) > 10:
                last = self.end.prev
                last.prev.next = self.end
                self.end.prev = last.prev
                del self.dict[last.key]




lru = LRU()

lru.add('i', 'j')
lru.add('i', 'm')

print(lru)
print('s')
        
   
