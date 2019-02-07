# Manager Class

class Manager(object):

    def add(self):
        from item import Item
        self.print()
        print("What would you like to add?")
        newText = input("> ")
        item = Item(newText)
        todos = open("todos.txt", "a")
        todos.write(f"[{item.time}| ")
        todos.write(f"{item.text}]\n")
        print("Would you like to add another item?")
        answer = input("> ")
        if 'y' in answer:
            todos.close()
            self.add()
        else:
            todos.close()
            self.print()

    def print(self):
        todos = open("todos.txt", "r")
        print(todos.read())
        todos.close()

    def complete(self):
        #opens text file to read
        todos = open("todos.txt", "r")
        #sets lines equal to a list of strings of each task
        lines = todos.readlines()
        #initializes newLines, a new list to be printed
        newLines = []
        #prints list
        self.print()
        #question
        print("Which item have you completed?")
        #sets input as a number called answer
        answer = int(input("> "))
        #closes file
        todos.close()
        #re-opens file to rewrite
        todos = open("todos.txt", "w")
        #cycles through each task in the "lines" list
        for line in lines:
            #sets index equal to the index(number) of each line
            index = lines.index(line) + 1
            #if the index is equal to the answer given...
            if index != answer:
                # add the line to the list of newLines
                newLines.append(line)
        #cycles through each line in the adjusted text
        for line in newLines:
            #prints each line
            todos.write(line)
        #Question
        print("Is there anything else you have completed?")
        #accepts input as complete
        complete = input("> ")
        #if yes...
        if 'y' in complete:
            #closes file
            todos.close()
            #reiterates
            self.complete()
        else:
            todos.close()
            self.print()

    #if nothing print nothing, if items print list

    #type "add *" and add list item of "*"
