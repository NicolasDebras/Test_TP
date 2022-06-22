from calendar import day_abbr
from user_file import user
import datetime


def test_old_user():
    bob = user("nicolas", 'nico@genie.com', datetime.date.today()-datetime.timedelta(days=365*20))
    test = bob.isValid()
    assert test == True

def test_young_user():
    bob = user("nicolas", 'nico@genie.com', datetime.date.today())
    test = bob.isValid()
    assert test == False

def test_empty_name_user():
    bob = user("", 'nico@genie.com',datetime.date.today()-datetime.timedelta(days=365*20))
    test = bob.isValid()
    assert test == False

def test_empty_email_user():
    bob = user("nico", '', datetime.date.today()-datetime.timedelta(days=365*20))
    test = bob.isValid()
    assert test == False

def test_nome_email_user():
    bob = user("nico", 'sdhfhjsjnfdisjfsdj', datetime.date.today()-datetime.timedelta(days=365*20))
    test = bob.isValid()
    assert test == False

def test_year_user():
    bob = user("nico", 'nico@toto.com', datetime.date.today()-datetime.timedelta(days=365*13 + 1))
    test = bob.isValid()
    assert test == True



