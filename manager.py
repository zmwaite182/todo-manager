# Manager Class

class Manager(object):

    def guide(self):
        print("What would you like to do?")
        print("1. View List")
        print("2. Add to List")
        print("3. Complete Task on list")
        print("4. Remove Task from list")
        print("5. Quit")
        choice = input("> ")
        if int(choice) == 1:
            self.print()
        elif int(choice) == 2:
            self.add()
        elif int(choice) == 3:
            self.complete()
        elif int(choice) == 4:
            self.remove()
        elif int(choice) == 5:
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
        todos.write(f"{item.completed}|{item.text}|{item.time}\n")
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
        lines = todos.readlines()
        for line in lines:
            index = lines.index(line) + 1
            innerLine = line.split('|')
            if innerLine[0] == str(True):
                print(f"\u221a|{index}. {innerLine[1]}|{innerLine[2]}")
            else:
                print(f"\u0d4f|{index}. {innerLine[1]}|{innerLine[2]}")
        todos.close()

    def complete(self):
        todos = open("todos.txt", "r")
        lines = todos.readlines()
        todos.close()
        self.print()
        print("Which item have you completed?(line #)")
        answer = int(input("> "))
        todos = open("todos.txt", "w")
        for line in lines:
            index = lines.index(line) + 1
            innerLine = line.split('|')
            if index == answer:
                innerLine[0] = str(True)
                line = '|'.join(innerLine)
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

    def remove(self):
        todos = open("todos.txt", "r")
        lines = todos.readlines()
        todos.close()
        self.print()
        print("Which line would you like to remove?(line #)")
        answer = int(input("> "))
        todos = open("todos.txt", "w")
        for line in lines:
            index = lines.index(line) + 1
            if index != answer:
                todos.write(line)
        print("Is there anything else you would like to remove?")
        answer2 = input("> ")
        if 'y' in answer2:
            todos.close()
            self.remove()
        else:
            todos.close()
            self.print()
        self.guide()
