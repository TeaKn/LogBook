import bottle

@bottle.get('/static/<datoteka:path>')
def static(datoteka):
    return bottle.static_file(datoteka, root='static')

@bottle.get('/')
@bottle.view('index.html')
def index():
    pass

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True, reloader=True)