from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Atharv Ganer" 
    pnr = "240840141004" 
    return render_template('index.html', name=name, pnr=pnr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  
