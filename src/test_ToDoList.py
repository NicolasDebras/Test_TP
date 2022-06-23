from datetime import datetime
from datetime import timedelta
from datetime import date
from ToDoList import sendMail
from ToDoList import ToDoList
from Item import Item
from user_file import user
from io import StringIO
import sys

#verification si deux taches ont des dates différente de 30 min : date + 35 min donc resultat true
def test_verif_date_correct():
    item1 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+ timedelta(minutes=35))
    previousItem = Item("Tache 2", 'prevoir 31 minutes' , datetime.now())
    test = ToDoList.verifdate(item1, previousItem)
    assert True == test

#verification si deux taches ont des dates différente de 30 min : date + 29 min donc resultat false
def test_verif_date_not_correct():
    item1 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=29))
    previousItem = Item("Tache 2", 'prevoir 31 minutes' , datetime.now())
    test = ToDoList.verifdate(item1, previousItem)
    assert False == test


#verification si deux taches ont des dates différente de 30 min : date + 0 min donc resultat false
def test_verif_date_0():
    item1 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=0))
    previousItem = Item("Tache 2", 'prevoir 31 minutes' , datetime.now())
    test = ToDoList.verifdate(item1, previousItem)
    assert False == test

#verification focntion verifName : si dans la liste aucun ne possède le meme nom : pas de nom de identique 
def test_verif_name_not_correct():
    item1 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=31))
    previousItem = Item("Tache 2", 'prevoir 31 minutes' , datetime.now())
    itemtoADD = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=62))
    list = [previousItem, item1]
    test = ToDoList.verifName(itemtoADD, list)
    assert False == test

#verification focntion verifName : si dans la liste aucun ne possède le meme nom : nom identique
def test_verif_name_correct():
    item1 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=31))
    previousItem = Item("Tache 2", 'prevoir 31 minutes' , datetime.now())
    itemtoADD = Item("Tache 3", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=62))
    list = [previousItem, item1]
    test = ToDoList.verifName(itemtoADD, list)
    assert True == test

#verification focntion verifName : si dans la liste aucun ne possède le meme nom : liste vide 
def test_verif_list_void():
    itemtoADD = Item("Tache 3", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=62))
    list = []
    test = ToDoList.verifName(itemtoADD, list)
    assert True == test

#verification si la ToDoList se contruit bien 
def test_verif_add_item_to_ToDoListe():
    items = Item("Tache 2", 'prevoir 31 minutes' , datetime.now())
    item2 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=31))
    item3 = Item("Tache 3", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=62))
    list = [items, item2, item3]
    bob = user("nicolas", 'nico@genie.com', date.today()-timedelta(days=365*20), 'nicolasLemeilleur')
    Todo = ToDoList(bob)
    Todo.addItem(items)
    Todo.addItem(item2)
    Todo.addItem(item3)
    assert list == Todo.Itemstab

#verification si la a ToDoList se contruit bien en expluant la tache avec le meme nom
# verifie si la fonction additem a bien renvoyé nul et que la taille du tableau de tache est de 2
def test_verif_add_item_to_ToDoListe_not_correct():
    items = Item("Tache 2", 'prevoir 31 minutes' , datetime.now())
    item2 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=31))
    item3 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=62))
    bob = user("nicolas", 'nico@genie.com', date.today()-timedelta(days=365*20), 'nicolasLemeilleur')
    Todo = ToDoList(bob)
    Todo.addItem(items)
    Todo.addItem(item2)
    test = Todo.addItem(item3)
    assert test == False
    assert 2 == len(Todo.Itemstab)

#verification si la a ToDoList se contruit bien en expluant la tache sans nom
def test_verif_add_item_to_ToDoListe_empty_name():
    items = Item("Tache 2", 'prevoir 31 minutes' , datetime.now())
    item2 = Item("Tache 1", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=31))
    item3 = Item("", 'prevoir 30 minutes' , datetime.now()+timedelta(minutes=62))
    bob = user("nicolas", 'nico@genie.com', date.today()-timedelta(days=365*20), 'nicolasLemeilleur')
    Todo = ToDoList(bob)
    Todo.addItem(items)
    Todo.addItem(item2)
    test = Todo.addItem(item3)
    assert test == False

#verification si la toDolist peut bien prendre que 10 élement 
def test_verif_11_item_into_ToDoList():
    itemtab = []
    for i in range(0, 100):
     itemtab.append(Item("Tache " + str(i), 'prevoir 31 minutes' , datetime.now()+timedelta(minutes=31*i)))
    bob = user("nicolas", 'nico@genie.com', date.today()-timedelta(days=365*20), 'nicolasLemeilleur')
    Todo = ToDoList(bob)
    for element in itemtab:
        Todo.addItem(element)
    assert 10 == len(Todo.Itemstab)

#verification ajout d'un utilisateur qui n'est pas correcte 
def test_verif_user_not_correct():
    bob = user("nicolas", 'nico@genie.com', date.today(), 'nicolasLemeilleur')
    capturedOutput = StringIO()          # Create StringIO object
    sys.stdout = capturedOutput                   #  and redirect stdout.
    Todo = ToDoList(bob)
    sys.stdout = sys.__stdout__                   # Reset redirect.
    assert "utilisateur non valide\n" == capturedOutput.getvalue()

#verification ajout d'un utilisateur qui est correcte 
def test_verif_user_correct():
    bob = user("nicolas", 'nico@genie.com', date.today()-timedelta(days=365*20), 'nicolasLemeilleur')
    capturedOutput = StringIO()          # Create StringIO object
    sys.stdout = capturedOutput                   #  and redirect stdout.
    Todo = ToDoList(bob)
    sys.stdout = sys.__stdout__                   # Reset redirect.
    assert "" == capturedOutput.getvalue()

#verifie si checkLenghtContent renvoie False qaund content fais plus de 200 caractères
def test_item_not_correct():
    item = Item("Tache 2", 'qsfldhqsgfsjhfsdhfsdhhfjsdhghhhhhhghghghghghhghghghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhfhodsfhsdfsdfhsdfsddfsfsdfsfsfsfgggggggggggggggggggggggggggggggggggggggggggggggggggggdfugsfuhsfusdfusdfusdfuysdfsdufusfysdfdsufysdfuyu' , datetime.now())
    assert False == Item.checkLenghtContent(item.content)

#verifie si checkLenghtContent renvoie True qaund content fais moins de 200 caractères
def test_item_not_correct():
    item = Item("Tache 2", '1' , datetime.now())
    assert True == Item.checkLenghtContent(item.content)

#verifie si checkLenghtContent renvoie True qaund content fais moins de 200 caractères
def test_item_not_correct():
    item = Item("Tache 2", '1' , datetime.now())
    assert True == Item.checkLenghtContent(item.content)

#verifie si checkLenghtContent renvoie False qaund content est vide 
def test_item_not_correct_0():
    item = Item("Tache 2", '', datetime.now())
    assert False == Item.checkLenghtContent(item.content)

#--------------------------------------------MOCKER---------------------------------------------------------------------

#FAKE le return de la fonction ToDoList.sendMail qui se declenche lors de l'ajout d'une 8 taches 
def test_8_Item_to_ToDo(mocker):
    mocker.patch('ToDoList.sendMail', return_value='EMAIL ENVOYE')
    itemtab = []
    for i in range(0, 6):
        itemtab.append(Item("Tache " + str(i), 'prevoir 31 minutes' , datetime.now()+timedelta(minutes=31*i)))
    bob = user("nicolas", 'nico@genie.com', date.today()-timedelta(days=365*20), 'nicolasLemeilleur')
    Todo = ToDoList(bob)
    for element in itemtab:
        Todo.addItem(element)
    item7 = Item("Tache 8", 'prevoir 31 minutes' , datetime.now()+timedelta(minutes=1440))
    test = Todo.addItem(item7)
    assert 'EMAIL ENVOYE' == test

