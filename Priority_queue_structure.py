class Element:

    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet

    def __lt__(self,other):
        if self.__priorytet < other.__priorytet:
            return True
        return False
    
    def __gt__(self,other):
        if self.__priorytet > other.__priorytet:
            return True
        return False
   
    def __repr__(self):
        output = f"{self.__priorytet} : {self.__dane}"
        return output
    
class PriorityQueue:
    
    def __init__(self):
        self.tab = []
        self.heap_size = 0
    
    def left(self, index):
        return 2*index+1
    
    def right(self,index):
        return 2*index+2
    
    def parent(self,index):
        return (index - 1) // 2

    def is_empty(self):
        if self.heap_size == 0:
            return True
        return False
   
    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]
    
    def enqueue(self, element: Element):
        if self.heap_size >= len(self.tab):
            self.tab.append(element)
        else:
            self.tab[self.heap_size] = element
            
        idx = self.heap_size
        self.heap_size += 1

        while idx > 0:
            p_idx = self.parent(idx)
            if self.tab[idx] > self.tab[p_idx]:
                self.tab[idx], self.tab[p_idx] = self.tab[p_idx], self.tab[idx]
                idx = p_idx
            else:
                break
    
    def dequeue(self):
        if not self.heap_size:
            return None
            
        top_item = self.tab[0]

        last_idx = self.heap_size - 1
        self.tab[0] = self.tab[last_idx]
        self.heap_size -= 1
        
        if self.heap_size > 1:
            self.fix_heap(0)
            
        return top_item
    
    def fix_heap(self, idx):
        while True:
            left_child = self.left(idx)
            right_child = self.right(idx)
            target = idx

            if left_child < self.heap_size and self.tab[left_child] > self.tab[target]:
                target = left_child
            if right_child < self.heap_size and self.tab[right_child] > self.tab[target]:
                target = right_child

            if target != idx:
                self.tab[idx], self.tab[target] = self.tab[target], self.tab[idx]
                idx = target
            else:
                break
    
    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.heap_size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)
    
if __name__ == "__main__":

    pq = PriorityQueue()
        
    priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    chars = "GRYMOTYLA"
        
    for p, c in zip(priorities, chars):
        pq.enqueue(Element(c, p))

    pq.print_tree(0, 0)

    pq.print_tab()
        
    first_removed = pq.dequeue()
        
    print(pq.peek())
        
    pq.print_tab()
        
    print(first_removed)
        
    while not pq.is_empty():
        print(pq.dequeue())
            
    pq.print_tab()