# Item Class

class Item(object):

    def __init__(self, text):
        import datetime
        now = datetime.datetime.now()
        self.time = (f"{now.year}-{now.month}-{now.day}")
        self.completed = False
        self.text = text
