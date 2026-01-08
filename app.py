from flask import Flask, render_template, request, redirect, url_for
from models import trucks

app = Flask(__name__)
@app.route("/about")
def about(): 
    return "Acerca de Truck"


# Página principal: lista de camiones

@app.route("/admin")
def admin(): 
     return render_template("admin.html")
    
@app.route("/truck") 
def conductor(): 
    return "<h1>Bienvenido Conductor</h1>"



@app.route("/")
def index():
    return render_template("index.html", trucks=trucks)

# Crear un nuevo camión
@app.route("/add", methods=["GET", "POST"])
def add_truck():
    if request.method == "POST":
        new_id = len(trucks) + 1
        trucks.append({
            "id": new_id,
            "marca": request.form["marca"],
            "modelo": request.form["modelo"],
            "año": request.form["año"]
        })
        return redirect(url_for("index"))
    return render_template("add_truck.html", title="Agregar Camión")


# Editar un camión
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_truck(id):
    truck = next((t for t in trucks if t["id"] == id), None)
    if request.method == "POST":
        truck["marca"] = request.form["marca"]
        truck["modelo"] = request.form["modelo"]
        truck["año"] = request.form["año"]
        return redirect(url_for("index"))
    return render_template("edit_truck.html", truck=truck)

# Eliminar un camión
@app.route("/delete/<int:id>", methods=["GET", "POST"]) 
def delete_truck(id): 
    truck = next((t for t in trucks if t["id"] == id), None) 
    if request.method == "POST": 
        trucks.remove(truck) # ✔️ elimina directamente sin global 
        return redirect(url_for("index")) 
    return render_template("delete_truck.html", truck=truck)

if __name__ == "__main__":
    app.run(debug=True)
