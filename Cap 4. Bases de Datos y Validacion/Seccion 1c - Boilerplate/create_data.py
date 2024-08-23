from application import db
db.create_all()

from application import User
user1=User(username='Bjørk')
db.session.add(user1)
user2=User(username='Fjell')
db.session.add(user2)
db.session.commit()


from application import Frase
frase1 = Frase(frase="Hola mundo", user_id=user1.id)
frase2 = Frase(frase="Ciao mundo", user_id=user1.id)
db.session.add(frase1) 
db.session.add(frase2) 
frase3 = Frase(frase="Mi casa es grande", user_id=user2.id)
frase4 = Frase(frase="Mi perro es bonito", user_id=user2.id)
db.session.add(frase3) 
db.session.add(frase4) 
db.session.commit()

#Some basic queries
frase1 = Frase.query.first()
frase1.user_id
frase1.author
frase1.author.username
frase1.frase

#Erase tables and rows
#db.drop_all()