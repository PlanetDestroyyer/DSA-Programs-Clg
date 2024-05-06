class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Hashing:
    def __init__(self):
        self.hash_table = [None] * 10

    def hash_func(self,value):
        return value % 10

    def create_node(self,x):
        return Node(x)
        
    def display(self):
        for i in range(10):
            print(f"\na[{i}] : ",end=' ')
            temp = self.hash_table[i]
            while temp:
                print("->",temp.value,end=' ')
                temp = temp.next
            print()

    def search_element(self,value):
        flag = False
        hash_valu = self.hash_func(value)
        entry = self.hash_table[hash_valu]
        print("Elemet Found at : ", end=' ')
        while entry:
            if entry.value== value:
                print(f"{hash_valu} : {entry.value}")
                flag = True
            entry = entry.next
        if not flag:
            return -1


    def delete_elemet(self,value):
        hash_valu = self.hash_func(value)
        entry = self.hash_table[hash_valu]
        if entry is None:
            print("No element Found")
            return
        if entry.value == value:
            self.hash_table[hash_valu] = entry.next
            return
        while entry.next and entry.next.value != value:
            entry = entry.next
        if entry.next:
            entry.next = entry.next.next


    def insert_element(self,value):
        hash_valu = self.hash_func(value)
        head = self.create_node(hash_valu)
        temp = self.hash_table[hash_valu]
        if temp is None:
            self.hash_table[hash_valu] = head
        else:
            while temp.next:
                temp = temp.next
            temp.next = head

        

if __name__ == "__main__":
    h = Hashing()
    while True:
        print("Telephone")
        print("1)Inset\n 2)Dispaly\n 3)Search\n 4)Delete\n 5)Exit")
        choice = int(input("Enter the Choice : "))
        if choice == 1:
            data = int(input("Enter phone no. to be nserted : "))
            h.insert_element(data)
        elif choice == 2:
            h.display()
        elif choice == 3:
            search = int(input("Enter the no. to be searched : "))
            if h.search_element(search) == -1:
                print("No elememts found at key")
        
        elif choice == 4:
            del_value = int(input("Enter the element : "))
            h.delete_elemet(del_value)
            print("Phone no. Deleted")
        elif choice == 5:
            break
    
        else: 
            print("Error! Try Again ")
        