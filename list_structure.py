class ListLinked:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data):
        new_data = Elements(data)
        new_data.next = self.head
        self.head = new_data

    def append(self, data):
        new_data = Elements(data)
        if self.head is None:
            self.head = new_data
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_data

    def remove(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        return removed.data
    
    def remove_end(self):
        if self.head is None:
            return None

        if self.head.next is None:
            removed = self.head
            self.head = None
            return removed.data

        prev = None
        current = self.head

        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None
        return current.data
    
    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def length(self):
        if self.head is None:
            return 0
        counter = 1
        current = self.head
        while current.next is not None:
            current = current.next
            counter += 1
        return counter
    
    def get(self):
        if self.head is None:
            return None
        return self.head.data

    def __str__(self):
        if self.head is None:
            return ""
        output = ""
        current = self.head
        while current is not None:
            output += f"-> {current.data}\n"
            current = current.next
        return output.strip()



class Elements:
    def __init__(self,data):
        self.data = data
        self.next = None

def main():
    data = [('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]
    uczelnie = ListLinked()
    uczelnie.append(data[0])
    uczelnie.append(data[1])
    uczelnie.append(data[2])
    uczelnie.add(data[3])
    uczelnie.add(data[4])
    uczelnie.add(data[5])
    print(uczelnie)
    print()
    print(uczelnie.length())
    print()
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print()
    print(uczelnie)
    uczelnie.destroy()
    print()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.append(('AGH', 'Kraków', 1919))
    uczelnie.remove_end()
    print()
    print(uczelnie.is_empty())


if __name__ == "__main__":
    main()