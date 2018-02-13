from flask import Flask, request
from flask import render_template

app = Flask(__name__)

contacts = {
    'Ceris' : {'name': 'Ceris', 'email': 'ceris@example.com', 'phone': 'x12343'},
    'John': {'name': 'John', 'email': 'john@example.com', 'phone': 'x21423'},
    'Megan': {'name': 'Megan', 'email': 'megan@example.com', 'phone': 'x17000'},
    }


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        contacts[name] = ({'name': name, 'email': email, 'phone': phone})
    
    return render_template("index.html", contacts = contacts.values())



@app.route("/delete", methods=["POST"])
def delete_contact():
    name_to_delete = request.form.get('contact_to_delete')
    
    del(contacts[name_to_delete])
    
    return render_template("index.html", contacts = contacts.values())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)