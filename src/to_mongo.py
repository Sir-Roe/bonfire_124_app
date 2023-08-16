#import statements
from base import Base
from dotenv import load_dotenv
import pymongo
import os

class ToMongo(Base):
    '''
    design class to transport the data from the base class
    to a mongo db instance. Initialized an instance of the inherite class

    defined methods are as follows
    upload_one_by_one: uploads pieces of information to a database over iterable structure
    upload_collection: upload an entire document of items to MongoDB
    delete_collection: drops an entire collection of data
    '''
    def __init__(self):
        Base.__init__(self)
        
        #load_dotenv()
        #self.user = os.getenv('USERNAME')
        #self.password = os.getenv('PASSWORD')
        self.mongo_url= 'mongodb+srv://lmproe27:SirRoe124@cluster0.zhnjqzj.mongodb.net/?retryWrites=true&w=majority'
        #connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)

        self.db = self.client.db
        self.cards = self.db.cards

        self.df.set_index('id', inplace=True)
    def upload_collection(self):
        '''
        upload an entire collection of items to MongoDB.
        BEWARE THERE IS A MAXIMUM UPLOAD SIZE
        limitations to the amount of data that you can upload at once
        '''
        self.cards.insert_many([self.df.to_dict()])

    def upload_one_by_one(self):
        '''
        upload all our items to db 1 by 1
        '''
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())
if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.upload_one_by_one()