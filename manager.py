# Manager Class

import item

class Manager(object):

    def add(self, item):
        todos = open("todos.txt", "a")
        todos.write(f"{item.time}\n")
        todos.write(f"{item.completed}\n")
        todos.write(f"{item.text}\n")

    #if nothing print nothing, if items print list

    #type "add *" and add list item of "*"
