class CyclicList:
    def __init__(self):
        self.size = 5
        self.list = [None for _ in range(self.size)]
        self.memory_i = 0
        self.reading_i = 0
    def is_empty(self):
        if self.memory_i == self.reading_i:
            return True
        return False
    def peek(self):
        if self.is_empty():
            return None
        return self.list[self.reading_i]
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.list[self.reading_i]
        self.list[self.reading_i] = None
        self.reading_i = (self.reading_i + 1) % self.size
        return value
    def enqueue(self,data):
        self.list[self.memory_i] = data
        self.memory_i = (self.memory_i +1) % self.size
        if self.memory_i == self.reading_i:
            old_size = self.size
            new_size = 2 * old_size
            new_list = [None for _ in range(new_size)]
            for i in range(0, self.memory_i):
                new_list[i] = self.list[i]
            shift = new_size - old_size
            for i in range(self.reading_i, old_size):
                new_list[i + shift] = self.list[i]
            self.list = new_list
            self.reading_i = self.reading_i + shift
            self.size = new_size
    def __str__(self):
        output = ""
        output += "[ " 
        for i in range(self.size):
            if self.list[i] == None:
                continue
            output += f"{self.list[i]} "
        output += "]"
        return output.strip()
    
def main():
    queue = CyclicList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.peek())
    print(queue)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    print(queue.list)
    while queue.is_empty() == False:
        print(queue.dequeue())
    print(queue)

if __name__ == "__main__":
    main()
    
