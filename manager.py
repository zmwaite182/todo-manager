# Manager Class

import item

class Manager(object):

    def add(self, item):
        todos = open("todos.txt", "a")
        todos.write(f"\n{item.time}")
        todos.write(f"\n{item.completed}")
        todos.write(f"\n{item.text}")

    def print(self):
        todos = open("todos.txt", "r")
        print(todos.read())

    #if nothing print nothing, if items print list

    #type "add *" and add list item of "*"
