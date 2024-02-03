# linked list 구현

# Head 값 가져야(초기값: null, 0x00000) → Head가 첫 번째 노드를 가리켜야 Linked List 완성

# node.py에서 구현해준 노드 클래스
class Node:
    def __inti__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # O(1)로 append 구현
    def append(self, value):
        new_node = Node(value)
        
        # head가 첫 번째 노드를 가리켜야
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤 노드가 new_node를 가리켜야
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    
    # head 접근 → 원하는 index 이동 → value 반환  
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

## insert_at 함수 -> Current를 New Node 직전까지 → New Node의 Next addres를 먼저 가리키게 → Current Node의 Next address를 New Node 가리킬 수 있게
## remove_at 함수 -> 제거하려는 노드의 앞 노드로 current, 실제 삭제 안해도 됨 → 파이썬에서 아무도 참조 안하면 Garbage Collector가 알아서 삭제

        