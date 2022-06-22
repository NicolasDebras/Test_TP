class EmailSenderService:
    def __init__(self, user, item):
        self.user = user
        self.item = item

    def sendMail(self):
        print(f" Send mail to {self.user.nom} ")
        print(f"It is only possible to add 2 items now for  {self.item.name}" )