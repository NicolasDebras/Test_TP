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
    
    def isValid(self):
        test =  datetime.date.today()  - self.DateNaissance
        print(datetime.date.today().strftime('%Y-%m-%d %H:%M:%S'))
        if ( test > datetime.timedelta(days=4745) and len(self.nom) !=  0 and self.check_email(self.email) == True) :
            return True
        return False


bob = user("nicolas", 'nico@gmail.com', datetime.date(2015, 6, 29))
print(bob.isValid())
