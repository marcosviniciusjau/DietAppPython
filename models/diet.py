class Diet:
    def __init__(self,id,name,description,date,hour,isOnDiet= False) -> None:
        self.id= id
        self.name= name
        self.description= description
        self.date= date,
        self.hour= hour
        self.isOnDiet= isOnDiet

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "hour": self.hour,
            "isOnDiet":self.isOnDiet
        }
    