# Item Class

import datetime

class Item(object):

    def __init__(self, text):
        self.time = datetime.datetime.now()
        self.completed = False
        self.text = text
