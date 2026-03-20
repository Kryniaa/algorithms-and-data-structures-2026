SIZE = 6
class Elem:
    def __init__(self):
        self.tab = [None for _ in range(SIZE)]

        self.elem_count = 0

        self.next = None

    def insert(self, data, ind):
        if self.elem_count >= SIZE:
            raise Exception("List is full")

        if ind < 0 or ind > self.elem_count:
            raise IndexError("Incorrect index")
        
        for i in range(self.elem_count, ind, -1):
            self.tab[i] = self.tab[i - 1]

        self.tab[ind] = data
        self.elem_count += 1

    def delete(self, ind):
        if ind < 0 or ind >= self.elem_count:
            raise IndexError("Incorrect index")

        for i in range(ind, self.elem_count - 1):
            self.tab[i] = self.tab[i + 1]

        self.tab[self.elem_count - 1] = None
        self.elem_count -= 1

class ULinkedList:
    def __init__(self):
        self.head = None
    def get(self,ind):
        if ind<0:
            raise IndexError("Incorrect index")
        
        node = self.head

        while node:
            if ind<node.elem_count:
                return node.tab[ind]
            else:
                ind -= node.elem_count
                node = node.next
        
        return None
    
    def insert(self,data,ind):
        if ind<0:
            raise IndexError("Incorrect index")
        
        if self.head is None:
            node = Elem()
            node.insert(data,0)
            self.head = node
            return
        
        node = self.head
        prev = None

        while node:
            if ind <= node.elem_count:
                break
            ind -= node.elem_count
            prev = node
            node = node.next
        
        if node is None:
            node = prev
            ind = node.elem_count
        
        if node.elem_count < SIZE:
            node.insert(data,ind)
            return
        
        new_node = Elem()
        mid = SIZE//2

        for i in range(mid, SIZE):
            new_node.tab[i - mid] = node.tab[i]

        new_node.elem_count = SIZE - mid
        node.elem_count = mid

        for i in range(mid, SIZE):
            node.tab[i] = None

        new_node.next = node.next
        node.next = new_node

        if ind <= node.elem_count:
            node.insert(data, ind)
        else:
            new_node.insert(data, ind - node.elem_count)

    def delete(self, ind):
        if self.head is None:
            raise IndexError("List is empty")

        node = self.head

        while node:
            if ind < node.elem_count:
                break
            ind -= node.elem_count
            node = node.next

        if node is None:
            raise IndexError("Incorrect index")

        node.delete(ind)

        half = SIZE // 2
        next_node = node.next

        if node.elem_count < half and next_node:

            needed = half - node.elem_count
            to_move = min(needed, next_node.elem_count)

            for i in range(to_move):
                node.insert(next_node.tab[i], node.elem_count)

            for i in range(to_move, next_node.elem_count):
                next_node.tab[i - to_move] = next_node.tab[i]
            for i in range(next_node.elem_count - to_move, next_node.elem_count):
                next_node.tab[i] = None
            next_node.elem_count -= to_move

            if next_node.elem_count < half:
                for i in range(next_node.elem_count):
                    node.insert(next_node.tab[i], node.elem_count)
                node.next = next_node.next
                next_node = None
    
    def print_list(self):
        node = self.head
        result = []
        while node:
            result.append(node.tab[:node.elem_count])
            node = node.next
        print(result)

def main():
    ull = ULinkedList()
    for i in range(1, 10):
        ull.insert(i, i-1)
    ull.print_list()
    print(ull.get(4))
    ull.insert(10, 1)
    ull.insert(11, 8)
    ull.print_list()
    ull.delete(1)
    ull.delete(2)
    ull.print_list()        

if __name__ == "__main__":
    main()