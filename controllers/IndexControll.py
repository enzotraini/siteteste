from main import app 

@app.route('/', methods=['GET'])
def index():
    return 'aqui ficaria o site do meu pai'