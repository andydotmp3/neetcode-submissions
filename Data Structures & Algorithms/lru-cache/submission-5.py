class DLLNode:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.head = DLLNode(-1, -1, None, None)
        self.tail = DLLNode(-1, -1, None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity
        self.size = 0

        

    def get(self, key: int) -> int:
        # print(f"get: {key=}")
        # print(f"  - {self.head.next.value=}")
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        # h -> A -> B -> C -> D -> t
        # into
        # h -> A -> C -> D -> B -> t
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        # print(f"  - {self.head.next.value=}")
        return node.value
        

    def put(self, key: int, value: int) -> None:
        # print(f"put: {key=}, {value=}")
        # print(f"  - {self.mapping.keys()=}")
        # print(f"  - {self.head.next.value=}")
        if self.get(key) == -1:
            node = DLLNode(key, value, self.tail.prev, self.tail)
            self.tail.prev.next = node
            self.tail.prev = node
            self.mapping[key] = node
            self.size += 1
        else:
            self.mapping[key].value = value


        if self.size > self.cap:
            eviction = self.head.next
            # print(f"  - {eviction.value=}")
            self.head.next = eviction.next
            eviction.next.prev = self.head
            # print(f"  - {self.head.next.value=}")
            del self.mapping[eviction.key]
            self.size -= 1
            return
        
        # print(f"  - {self.head.next.value=}")

        
