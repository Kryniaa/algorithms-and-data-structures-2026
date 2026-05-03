
import random
import time

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
    
    def __init__(self, tab):
        if tab is None:
            self.tab = []
            self.heap_size = 0
        else:
            self.tab = tab
            self.heap_size = len(tab)
            for i in range(self.heap_size // 2 - 1, -1, -1):
                self.fix_heap(i)
    
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
        self.tab[0], self.tab[last_idx] = self.tab[last_idx], self.tab[0]
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
    


def heap_sort(tab):
    pq = PriorityQueue(tab)

    while pq.heap_size > 0:
        pq.dequeue()

    return tab  

def selection_sort_swap(tab):
    for i in range(0,len(tab)-1):
        m = min(tab[i:])
        idxm = tab[i:].index(m) + i
        tab[i], tab[idxm] = tab[idxm], tab[i]
    return tab

def selection_sort_shift(tab):
    for i in range(0,len(tab)-1):
        m = min(tab[i:])
        idxm = tab[i:].index(m) + i
        element = tab.pop(idxm)
        tab.insert(i, element)
    return tab

def insertion_sort(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab

def shell_sort_classic(tab):
    h = len(tab) // 2
    l = len(tab)
    
    while h > 0:
        for i in range(h, l):
            key = tab[i] 
            j = i
            while j >= h and tab[j - h] > key:
                tab[j] = tab[j - h]
                j -= h
            tab[j] = key
        h //= 2
    return tab

def shell_sort_knuth(tab):
    h = 1
    l = len(tab)
    while h < l // 3:
        h = 3 * h + 1
        
    while h >= 1:
        for i in range(h, l):
            key = tab[i]
            j = i
            while j >= h and tab[j - h] > key:
                tab[j] = tab[j - h]
                j -= h
            tab[j] = key
        h //= 3
    return tab

def main():
    choice = input("Choose the test 1/2: ")
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    
    match choice:
        case "1":
            tab_heap = [Element(v, k) for k, v in data]
            print("HEAP SORT")
            heap = PriorityQueue(tab_heap)
            heap.print_tab()
            heap.print_tree(0, 0)
            heap_sort(tab_heap)
            print(tab_heap)
            print("NIESTABILNE")

            print("INSERTION SORT")
            tab_ins = [Element(v, k) for k, v in data]
            insertion_sort(tab_ins)
            print(tab_ins)
            print("STABILNE")

            print("SHELL SORT (first version)")
            tab_sh_c = [Element(v, k) for k, v in data]
            shell_sort_classic(tab_sh_c)
            print(tab_sh_c)
            print("NIESTABILNE")

            print("SHELL SORT (second version)")
            tab_sh_k = [Element(v, k) for k, v in data]
            shell_sort_knuth(tab_sh_k)
            print(tab_sh_k)
            print("NIESTABILNE")

        case "2":
            n_elements = 10000
            base_tab = []
            for i in range(n_elements):
                base_tab.append(Element("data", int(100 * random.random())))

            tab1 = base_tab.copy()
            tab2 = base_tab.copy()
            tab3 = base_tab.copy()
            tab4 = base_tab.copy()


            t_start = time.perf_counter()
            insertion_sort(tab1)
            t_stop = time.perf_counter()
            print("HEAP SORT:")
            print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

            t_start = time.perf_counter()
            shell_sort_classic(tab2)
            t_stop = time.perf_counter()
            print("INSERTION SORT:")
            print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

            t_start = time.perf_counter()
            shell_sort_knuth(tab3)
            t_stop = time.perf_counter()
            print("SHELL SORT (first version):")
            print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

            t_start = time.perf_counter()
            heap_sort(tab4)
            t_stop = time.perf_counter()
            print("SHELL SORT (second version):")
            print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

if __name__ == "__main__":
    main()
