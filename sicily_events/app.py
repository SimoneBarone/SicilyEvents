from flask import Flask, render_template

app = Flask(__name__)

# Configurazione Base
app.config['SECRET_KEY'] = 'chiave_segreta_per_sicurezza'

# DATI GLOBALI (Single Source of Truth)
# Questo risponde all'esigenza di professionalità: dati coerenti ovunque.
SITE_DATA = {
    "name": "Sicily Events",
    "tagline": "Exclusive Weddings & Corporate DMC",
    "email": "info@sicilyevents.com",
    "phone": "+39 095 000 000",
    "instagram": "https://instagram.com/sicilyevents",
    "nav_items": [
        {"name": "Home", "url": "home"},
        {"name": "DMC Sicily", "url": "weddings"},
        {"name": "To Do", "url": "corporate"},
        {"name": "The Team", "url": "experiences"},
        {"name": "Contact", "url": "contact"}
    ]
}

@app.route('/')
def home():
    # Passiamo i dati alla Home Page
    return render_template('index.html', site=SITE_DATA, title="Home")

@app.route('/weddings')
def weddings():
    return "<h1>Pagina Weddings (in costruzione)</h1>"

@app.route('/corporate')
def corporate():
    return "<h1>Pagina Corporate (in costruzione)</h1>"

@app.route('/experiences')
def experiences():
    return "<h1>Pagina Experiences (in costruzione)</h1>"

@app.route('/contact')
def contact():
    return "<h1>Pagina Contatti (in costruzione)</h1>"

if __name__ == '__main__':
    app.run(debug=True)