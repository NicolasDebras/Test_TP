from datetime import datetime
from datetime import timedelta
from datetime import date
from traceback import print_tb
from user_file import user
from Item import Item


class ToDoList:

    #Constructeur : verifie si user est valide 
    def __init__(self, user ):
        if user.isValid() == True:
            self.user = user
        else:
            print("utilisateur non valide")
        self.Itemstab = []

    #constructeur ajout d'un item dans la ToDoLIst si l'item respecte les réglès
    def addItem(self, item):
        if Item.checkLenghtContent(item.content) == False or len(self.Itemstab) >= 10:
            return False
        if len(self.Itemstab) > 0:
            if ToDoList.verifdate(item, self.Itemstab[-1]) == False:
                return False
        if ToDoList.verifName(item, self.Itemstab) == False:
            return False
        self.Itemstab.append(item)
        if len(self.Itemstab) == 7:
            return sendMail()
        return True
    
    #verifie si la difference de date est superieur a 30 minutes 
    def verifdate(additem, Olditem):
        if (additem.date - Olditem.date) < timedelta(minutes=30):
            return False
        return True
    
    #verifie si deux le nom de additem est pas présent dans la liste et si le nom est pas vide 
    def verifName(addItem, listItem):
        if len(addItem.name) == 0:
            return False
        for element in listItem:
            if element.name == addItem.name:
                return False
        return True 

#Partie pour le MOCKER 
def sendMail():
    print("A DEV")

itemtab = []
for i in range(0, 7):
    itemtab.append(Item("Tache " + str(i), 'prevoir 31 minutes' , datetime.now()+timedelta(minutes=31*i)))
bob = user("nicolas", 'nico@genie.com', date.today()-timedelta(days=365*20), 'nicolasLemeilleur')
Todo = ToDoList(bob)
for element in itemtab:
    Todo.addItem(element)
item7 = Item("Tache 7", 'prevoir 31 minutes' , datetime.now()+timedelta(minutes=1440))
print(len(Todo.Itemstab))