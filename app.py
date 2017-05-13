from flask import Flask, current_app, render_template, request, json
from translate import tradutor

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/translate', methods=['POST', 'GET'])
def translate():
    texto = request.form['texto'];
    source = request.form['source'];
    target = request.form['target'];
    
    traduzido = tradutor(texto,source,target)
    return json.dumps({'':'','':traduzido});
    print(traduzido)

if __name__ == "__main__":
    app.run()
