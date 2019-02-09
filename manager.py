# Manager Class

class Manager(object):

    def guide(self):
        print("What would you like to do?")
        print("1. View List")
        print("2. Add to List")
        print("3. Complete Task on list")
        print("4. Quit")
        choice = input("> ")
        if int(choice) == 1:
            self.print()
        elif int(choice) == 2:
            self.add()
        elif int(choice) == 3:
            self.complete()
        elif int(choice) == 4:
            exit(0)
        else:
            self.guide()

    def add(self):
        from item import Item
        self.print()
        print("What would you like to add?")
        newText = input("> ")
        item = Item(newText)
        todos = open("todos.txt", "a")
        todos.write(f"[{item.time}|{item.text}]\n")
        print("Would you like to add another item?")
        answer = input("> ")
        if 'y' in answer:
            todos.close()
            self.add()
        else:
            todos.close()
            self.print()
        self.guide()

    def print(self):
        todos = open("todos.txt", "r")
        print(todos.read())
        todos.close()

    def complete(self):
        todos = open("todos.txt", "r")
        lines = todos.readlines()
        todos.close()
        self.print()
        print("Which item have you completed?(line #)")
        answer = int(input("> "))
        check = f"\u221a"
        newLines = []
        todos = open("todos.txt", "w")
        for line in lines:
            index = lines.index(line) + 1
            if index != answer:
                newLines.append(line)
            else:
                newLines.append(f"{check} {line}")
        for line in newLines:
            todos.write(line)
        print("Is there anything else you have completed?")
        complete = input("> ")
        if 'y' in complete:
            todos.close()
            self.complete()
        else:
            todos.close()
            self.print()
        self.guide()
