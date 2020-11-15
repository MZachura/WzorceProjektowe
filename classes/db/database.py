import pymongo
from pymongo import MongoClient
import pprint

class Database:
    _instance = None
    @staticmethod
    def get_instance():
        if Database._instance == None:
            Database()
        return Database._instance
    def __init__(self):
        self.cluster = MongoClient('localhost', 27017)
        self.db = self.cluster["shooterek"]
        self.scores = self.db["scores"]

        if Database._instance != None:
            raise Exception("To je singleton tego nie wywolasz 2 razy :)")
        else:
            Database._instance = self

    def add_score(self, player_name, score):
        to_send = {
            "Player_name": player_name,
            "score": score
        }

        self.scores.insert_one(to_send)
    
     # checks if there is more then 10 scores in db
    def update(self):
        result = self.checkDocAmount()
        while result > 10:
            self.findAllScores()
            self.findTheLowest()
            result = self.checkDocAmount()

    def findAllScores(self):
        self.results = []
        for result in self.scores.find({}, {"score": 1, "_id": 1}):
            self.results.append(result)

    
    # this func find & delete the lowest elemtnt
    def findTheLowest(self):
        lowest = self.results[0]
        for result in self.results:
            if lowest["score"] > result["score"]:
                lowest = result

        print("the lowest element is: ", lowest["_id"], lowest["score"])
        self.scores.delete_one({"_id": lowest["_id"]})

    
    def checkDocAmount(self):
        return self.scores.count_documents({})

    def loopfor10(self):
        # counter the number that cannot be exceed
        counter = 0
        # the list that will be returned
        highScores = [] 

        # loop through sorted results
        for result in self.scores.find({}).sort([("score", 1)]).limit(10):
            counter += 1
            # if exceed break
            if counter >= 11:
                break
            
            # maybe appending to the list and return it?
            #print(str(counter) + ". " ,result)
            highScores.append(result)


        # how many
        #print("the amount of docs: ",self.scores.count_documents({}))
        return highScores
    
    # delete all colections
    def clear(self):
        self.scores.delete_many({})

'''
def test():
    db= Database()
    
    db.add_score("Gary", 100)
    db.add_score("Gerul", 700)
    db.add_score("Jozek", 100)
    db.add_score("Jan", 250)
    db.add_score("Bace", 400)
    db.add_score("Jozek", 110)
    db.add_score("Gary", 140)
    db.add_score("Jozek", 300)
    db.add_score("Jozek", 900)
    db.add_score("Jozek", 320)
    
    temp = db.loopfor10()
    pprint.pprint(temp)

if __name__ == "__main__":
    test()

'''