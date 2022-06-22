import datetime
from datetime import  date

from src.EmailSenderService import EmailSenderService
from user_file import user
from Item import Item


class ToDoList:
    def __init__(self, user ,   item):
        self.user = user
        self.Items = item

    def addItem(self, item):
        if len(self.Items) > 10:
            return False
        if len(self.Items) > 0  and  item.date - self.Items[-1].date < datetime.timedelta(minutes=30):
            return False
        for i in range(0, len(self.Items)):
            if self.Items[i].name == item.name:
                return False
        print(item.name)
        self.Items.append(item)
        if len(self.Items) == 7:
            email = EmailSenderService(self.user, item)
            email.sendMail()
        return True





date1 = date(2015, 6, 29)

bob = user("nicolas", 'nico@gmail.com', date(2015, 6, 29), "password")
list = []
item1 = Item("nicolas2", 'nico@gmail.com', datetime.datetime(2021, 11, 11, 11, 42))
item2 = Item("nicolas2", 'nico@gmail.com', datetime.datetime(2021, 11, 12, 12, 42))
item3 = Item("nicolas4", 'nico@gmail.com', datetime.datetime(2021, 11, 13, 12, 42))
item4 = Item("nicolas5", 'nico@gmail.com', datetime.datetime(2021, 11, 14, 14, 42))
item5 = Item("nicolas6", 'nico@gmail.com', datetime.datetime(2021, 11, 15, 15, 42))
item6 = Item("nicolas7", 'nico@gmail.com', datetime.datetime(2021, 11, 16, 16, 42))
item7 = Item("nicolas8", 'nico@gmail.com', datetime.datetime(2021, 11, 17, 17, 42))
item8 = Item("nicolas9", 'nico@gmail.com', datetime.datetime(2021, 11, 17, 20, 42))
item9 = Item("nicolas10", 'nico@gmail.com', datetime.datetime(2021, 11, 18, 20, 42))
test = ToDoList(bob, list)
test.addItem(item1)
test.addItem(item2)
test.addItem(item3)
test.addItem(item4)
test.addItem(item5)
test.addItem(item6)
test.addItem(item7)
test.addItem(item8)
test.addItem(item9)
print(test.Items[0].name)
print(len(test.Items))
