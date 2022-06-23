import datetime
import re

class user:
    def __init__(self, nom, email, DateNaissance, password):
        self.email = email
        self.nom = nom
        self.DateNaissance = DateNaissance
        self.regex = '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$'
        self.password = password

    def printUser(self):
        print(self.DateNaissance.strftime('%Y-%m-%d %H:%M:%S'))

    def check_email(self, email):  
        if(re.search(self.regex,email)):  
            return True
        else:  
            return False

    def check_password(self):
        if len(self.password) > 7 and 41 > len(self.password):
            return True
        return False;
    
    def isValid(self):
        test =  datetime.date.today()  - self.DateNaissance
        if ( test > datetime.timedelta(days=4745) and len(self.nom) !=  0 and self.check_email(self.email) == True and self.check_password()) :
            return True
        return False



# bob = user("nicolas", 'nico@genie.com', datetime.date.today()-datetime.timedelta(days=365*20), 'nicolasLemeilleur')
# print(bob.check_password(), bob.password, len(bob.password));

