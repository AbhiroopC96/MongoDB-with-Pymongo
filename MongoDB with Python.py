# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:56:37 2021

@author: Abhiroop Chakraborty
"""

import pymongo
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['Authors']

information=mydb.authorsinformation

record=([{'firstname':'Randall',
          'lastname':'Munroe',
          },
         {'firstname':'David',
          'lastname':'Baldacci'
          },
         {'firstname':'Yuval',
          'lastname':'Harari'
          },
         {'firstname':'Rohinton',
          'lastname':'Mistry'
          },
         {'firstname':'Arundhati',
          'lastname':'Roy'
          },
          {'firstname':'Jordan',
          'lastname':'Peterson'
          },
          {'firstname':'Edward',
          'lastname':'Snowden'
          },
          {'firstname':'Richard',
          'lastname':'Ayoade'
          },
          {'firstname':'David',
          'lastname':'Spiegelhalter'}])


information.insert_many(record)


information.find_one()  #finds one data point from the db

for record in information.find(): #uses the cursor to get all the records
    print(record)
    
for record in information.find({'firstname':'Yuval'}):  #searching for a particular record
    print(record) #(Select firstname from Authors where firstname like 'Yuval')
    
    
#using the following expression $in,$lt,$gt

# '$in'
for record in information.find({'lastname':{'$in':['Roy','Ayoade']}}):
    print(record)

#lt - less than
#gt - greater than




