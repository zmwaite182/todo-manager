# Item Class

class Item(object):

    def __init__(self, text):
        import datetime
        self.time = datetime.datetime.now()
        self.completed = False
        self.text = text
