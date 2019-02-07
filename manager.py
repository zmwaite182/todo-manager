# Manager Class

class Manager(object):

    def add(self):
        from item import Item
        print("Would you like to add an item?")
        answer = input("> ")
        if 'y' in answer:
            print("What would you like to add?")
            newText = input("> ")
            item = Item(newText)
            todos = open("todos.txt", "a")
            todos.write(f"[{item.time}| ")
            todos.write(f"{item.text}]\n")
            self.add()

    def print(self):
        todos = open("todos.txt", "r")
        print(todos.read())

    #if nothing print nothing, if items print list

    #type "add *" and add list item of "*"
