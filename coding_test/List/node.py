# linked list 구현 전에 node 구현 먼저
# 1개 노드에는 데이터와 다음 노드 주소 담고 있다
# 마지막 노드는 다음에 가리킬 주소가 없으므로 null값

class Node:
    def __inti__(self, value=0, next=None):
        self.value = value
        self.next = next
        
first = Node(1)
second = Node(2)
third = Node(3)

# 첫번째 노드는 6, 두번째는 2, 세번째는 3을 갖고 있음
first.next = second
second.next = third
first.value = 6
        