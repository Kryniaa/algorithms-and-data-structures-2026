import random

class Node:
    def __init__(self, key, value, levels):
        self.key = key
        self.value = value
        self.levels = levels
        self.tab = [None] * levels
        
        
class Skiplist:
    def __init__(self, maxLevel):
        self.maxLevel = maxLevel
        self.p = 0.5
        self.head = Node(None,None,maxLevel)
    def randomLevel(self,p, maxLevel):
        lvl = 1   
        while random.random() < p and lvl <maxLevel:
            lvl = lvl + 1
        return lvl
    def search(self,key):
        current = self.head
        for i in range(self.maxLevel - 1, -1, -1):
                while current.tab[i] is not None and current.tab[i].key < key:
                    current = current.tab[i]

        current = current.tab[0]
        if current is not None and current.key == key:
            return current.value
        return None
    
    def insert(self,key,data):
        update = [None] * self.maxLevel
        current = self.head

        for i in range(self.maxLevel - 1, -1, -1):
                while current.tab[i] is not None and current.tab[i].key < key:
                    current = current.tab[i]
                update[i] = current
        current = current.tab[0]

        if current is not None and current.key == key:
            current.value = data
        else:
            new_lvl = self.randomLevel(self.p, self.maxLevel)
            new_node = Node(key, data, new_lvl)
            for i in range(new_lvl):
                new_node.tab[i] = update[i].tab[i]
                update[i].tab[i] = new_node

    def remove(self, key):
        update = [None] * self.maxLevel
        current = self.head
        for i in range(self.maxLevel - 1, -1, -1):
            while current.tab[i] is not None and current.tab[i].key < key:
                current = current.tab[i]
            update[i] = current

        current = current.tab[0]
        if current is not None and current.key == key:
            for i in range(self.maxLevel):
                if update[i].tab[i] != current:
                    break
                update[i].tab[i] = current.tab[i]
    
    def __str__(self):
        res = []
        current = self.head.tab[0]
        while current:
            res.append(f"({current.key}:{current.value})")
            current = current.tab[0]
        return " ".join(res)

    def displayList_(self):
        node = self.head.tab[0]
        keys = [ ]
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.maxLevel - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.value:2s}", end="")
                node = node.tab[lvl]
            print()

def Main():
    random.seed(42)
    sl1 = Skiplist(5)

    for i in range(1, 16):
        sl1.insert(i, chr(64 + i))

    sl1.displayList_()

    print(sl1.search(2))

    sl1.insert(2, 'Z')
    print(sl1.search(2))

    for k in [5, 6, 7]:
        sl1.remove(k)
    
    print(sl1)

    sl1.insert(6, 'W')
    print(sl1)

    random.seed(42)
    sl2 = Skiplist(5)

    for i in range(15, 0, -1):
        sl2.insert(i, chr(64 + i))

    sl2.displayList_()

    print(sl2.search(2))
    sl2.insert(2, 'Z')
    print(sl2.search(2))

    for k in [5, 6, 7]:
        sl2.remove(k)
    
    print(sl2)
    sl2.insert(6, 'W')
    print(sl2)

if __name__ == "__main__":
    Main()