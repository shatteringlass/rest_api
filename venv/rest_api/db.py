import models
from pony.orm import *

db = models.db

# pgsql
# db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='couplemoji')

# sqlite
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

# generate db mapping + create tables
db.generate_mapping(create_tables=True)

# create instances
with db_session:
    #l1 = models.Login(nickname='federico', password='prova')
    #l2 = models.Login(nickname='monica', password='avorp')
    #commit()
    #print("User1 login id is {}".format(l1.id))
    u1 = models.User(login=models.Login.get(nickname='federico').id)
    u2 = models.User(login=models.Login.get(nickname='monica').id)