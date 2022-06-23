from calendar import day_abbr
from user_file import user
from datetime import datetime


# TEST utilisateur correct 
def test_old_user():
    bob = user("nicolas", 'nico@genie.com', datetime.date.today()-datetime.timedelta(days=365*20), 'nicolasLemeilleur')
    test = bob.isValid()
    assert test == True

#test utilisateur trop jeune 
def test_young_user():
    bob = user("nicolas", 'nico@genie.com', datetime.date.today(), 'tototototot')
    test = bob.isValid()
    assert test == False

#test utilisateur sans nom
def test_empty_name_user():
    bob = user("", 'nico@genie.com',datetime.date.today()-datetime.timedelta(days=365*20), 'totototototot')
    test = bob.isValid()
    assert test == False

#test utilisateur sans email
def test_empty_email_user():
    bob = user("nico", '', datetime.date.today()-datetime.timedelta(days=365*20), 'totototototoototot')
    test = bob.isValid()
    assert test == False

#test utilsateur avec un mauvais email
def test_nome_email_user():
    bob = user("nico", 'sdhfhjsjnfdisjfsdj', datetime.date.today()-datetime.timedelta(days=365*20), 'totototootot')
    test = bob.isValid()
    assert test == False

#test utilisateur de 13 ans et un jour 
def test_year_user():
    bob = user("nico", 'nico@toto.com', datetime.date.today()-datetime.timedelta(days=365*13 + 1), 'totottotototoot')
    test = bob.isValid()
    assert test == True
