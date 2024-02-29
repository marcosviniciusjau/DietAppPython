from flask import Flask,request,jsonify
from models.diet import Diet
from repository.database import db
app= Flask(__name__)


app.config['SECRET_KEY']= "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://adm:&@127.0.0.1:3306/flask-crud'
db.init_app(app)

diets= []
diet_id_control= 1

@app.route("/diets", methods=['POST'])
def create_diet():
    global diet_id_control
    data= request.get_json()
    new_diet= Diet(id=diet_id_control,name=data["name"],description=data.get("description",""),date=data.get("date",""),hour=data.get("hour",""), isOnDiet=data.get("isOnDiet",False))
    diet_id_control +=1
    diets.append(new_diet)
    print(diets)
    return jsonify({"message":"Nova dieta criada com sucesso", "id": new_diet.id})

@app.route('/diets', methods=['GET'])
def get_diets():
    diet_list= [diet.to_dict() for diet in diets]
       
    output = {
    "diets": diet_list,
    "total_diets": len(diet_list)
   }
    return jsonify(output)

@app.route('/diets/<int:id>', methods=['GET'])
def get_diet(id):
    for t in diets:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Não foi possível encontrar a dieta"}),404

@app.route('/diets/<int:id>', methods=['PUT'])
def update_diet(id):
    diet = None
    for t in diets:
        if t.id == id:
            diet=t
    if diet is None:
        return jsonify({"message":"Não foi possível encontrar a dieta"}),404
    data= request.get_json()
    diet.name = data['name']
    diet.description = data['description']
    diet.date = data['date']
    diet.hour = data['hour']
    diet.isOnDiet = data['isOnDiet']
    print(diet)
    return jsonify({"message": "Dieta atualizada com sucesso"})

@app.route('/diets/<int:id>', methods=['DELETE'])
def delete_diet(id):
    diet = None
    for t in diets:
        if t.id == id:
            diet = t
            break

    if not diet:
        return jsonify({"message": "Não foi possível encontrar a dieta"}),404
    diets.remove(diet)
    return jsonify({"message": "Dieta excluída com sucesso!"})

if __name__ == "__main__":
    app.run(debug= True)
    
