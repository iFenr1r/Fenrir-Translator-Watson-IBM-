from flask import Flask, current_app, render_template, request, json, jsonify
from translate import tradutor, identificar
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/translate', methods=['POST', 'GET'])
def translate():
    texto = request.form['texto'];
    source = request.form['source'];
    target = request.form['target'];

    if source == 'identfy':
        traduzido = identificar(texto,target)
        
    else:
        traduzido = tradutor(texto,source,target)
    
    return jsonify(traduzido);
    print(traduzido)

if __name__ == "__main__":
    app.run()
