class Item:
    def __init__(self, name, content, date):
        self.name = name
        self.content = content
        self.date = date

    def checkLenghtContent(self):
        if len(self.content) > 200:
            return False
        else:
            return True

