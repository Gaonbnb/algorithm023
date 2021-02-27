

```python
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity 
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def put(self, key, value):
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        # 下面的两句颠倒位置就报错了
        self.head.next.prev = node
        self.head.next = node
        
        
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
```
