from flask import Flask, render_template, request
from utils.comissoes import main as calc_comissoes
from utils.movimentacoes import main as mov_estoque
from utils.juros import main as calc_juros

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/comissoes")
def comissoes():
    return render_template("comissoes.html")

@app.route("/calcular_comissoes")
def calcular_comissoes():
    calc_comissoes()
    return render_template("comissoes.html", msg="Cálculo executado! Veja o arquivo comissoes_result.json.")

@app.route("/movimentacoes", methods=["GET", "POST"])
def movimentacoes():
    if request.method == "POST":
        codigo = request.form["codigo"]
        quantidade = request.form["quantidade"]
        descricao = request.form["descricao"]

        import os
        os.system(f"python utils/movimentacoes.py {codigo} {quantidade} \"{descricao}\"")

        return render_template("movimentacoes.html", msg="Movimentação registrada!")
    return render_template("movimentacoes.html")

@app.route("/juros", methods=["GET", "POST"])
def juros():
    if request.method == "POST":
        valor = request.form["valor"]
        venc = request.form["venc"]

        import os
        os.system(f"python utils/juros.py {valor} {venc}")
        return render_template("juros.html", msg="Cálculo executado! Veja o console.")
    return render_template("juros.html")

if __name__ == "__main__":
    app.run(debug=True)

   