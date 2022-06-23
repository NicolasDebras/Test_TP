class Item:
    def __init__(self, name, content, date):
        self.name = name
        self.content = content
        self.date = date

    #verifie si la chaine de content fait plus de 200 caractère, revoie false si c'est le cas 
    def checkLenghtContent(content):
        if len(content) > 200 or len(content) == 0:
            return False
        else:
            return True

