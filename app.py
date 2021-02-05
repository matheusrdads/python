from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" and request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]

            if(request.form["opc"] == "soma"):
                soma =int(num1) + int(num2)
                return '<h1>O resultado da soma entre '+ str(num1) + ' e ' + str(num2) + ' é igual a ' + str(soma)+'</h1>'

            elif (request.form['opc'] == "subt"):
                subt =int(num1) - int(num2)
                return '<h1>O resultado da subtração entre '+ str(num1) + ' e ' + str(num2) + ' é igual a ' + str(subt)+'</h1>'

            elif (request.form['opc'] == "mult"):   
                mult =int(num1) * int(num2)
                return '<h1>O resultado da multiplicação entre '+ str(num1) + ' e ' + str(num2) + ' é igual a ' + str(mult)+'</h1>'

            else:
                divi =int(num1) // int(num2)
                return '<h1>O resultado da divisão entre '+ str(num1) + ' e ' + str(num2) + ' é igual a ' + str(divi)+'</h1>'
        else:
            return "<h1>informe um valor valido</h1>"

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

@app.errorhandler(405)
def not_found2(error):
    return "o verbo nao existe"

app.run(port=8081, debug=True)