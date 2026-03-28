class Elem:
    def __init__(self, key, value):
        self.value = value
        self.key = key
    def __str__(self):
        return f"{self.key}:{self.value}"

class Deleted:
    def __str__(self):
        return "None"

class HashTable:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.size = size
    def _modulo(self, key):
        counter = 0
        if isinstance(key,str):
            counter = sum(ord(char) for char in key)
            return counter % self.size
        else:
            return key % self.size
        
    def _hash_function(self,key,i):
        return (self._modulo(key) + self.c1 * i + self.c2 * (i**2)) % self.size

    def search(self, key):
        for i in range(self.size):
            index = self._hash_function(key, i)
            item = self.tab[index]
            
            if item is None:
                return None
            
            if isinstance(item, Deleted):
                continue
        
            if item.key == key:
                return item.value
        return None
    
    def insert(self, key, value):
        for i in range(self.size):
            index = self._hash_function(key, i)
            item = self.tab[index]

            if item is None or isinstance(item, Deleted):
                self.tab[index] = Elem(key, value)
                return
                
            if item.key == key:
                item.value = value
                return
            
        raise Exception("Brak miejsca")
    
    def remove(self,key):
        for i in range(self.size):
            index = self._hash_function(key, i)
            item = self.tab[index]
            
            if item is None:
                return None
            
            if isinstance(item, Deleted):
                continue
            
            if item.key == key:
                self.tab[index] = Deleted()
                return
        
        raise Exception("Brak danej")

    def __str__(self):
        elements = []
        for item in self.tab:
            if item is None:
                elements.append("None")
            else:
                elements.append(str(item))
        return "{" + ", ".join(elements) + "}"

def f1(size, c1=1, c2=0):
    tab = HashTable(size,c1,c2)
    tabl = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(1,size+1):
        if i == 6:
            tab.insert(18,tabl[i-1])
        elif i == 7:
            tab.insert(31,tabl[i-1])
        else:
            tab.insert(i,tabl[i-1])
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(5,'Z')
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    try:
        tab.insert("test", "W")
    except Exception as e:
        print(e)
    print(tab)

def f2(size,c1=1,c2=0):
    tab = HashTable(size,c1,c2)
    tabl = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(1,size+1):
        tab.insert(i*13,tabl[i-1])
    print(tab)

def main():
    f1(15)
    print()
    f2(15)
    print()
    f2(15,0,1)
    print()
    f1(15,0,1)
    

if __name__ == "__main__":
    main()