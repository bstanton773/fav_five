from app import app


@app.route('/')
def index():
    return 'Hello World'


@app.route('/favorites')
def favorites():
    return 'Favorites'
