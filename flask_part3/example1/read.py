from email import message
from app import Message

all_messages = Message.query.all()
print(all_messages)

#  [Jonas - jonas@mail.com, Antanas - antanas@mail.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]

# for message in all_messages: #print all text messages
#     print(message.message)
    
# message_1 = Message.query.get(1) #print first ID message
# print(message_1.message)  
    
message_marius = Message.query.filter_by(name="Marius").all()
print(message_marius)