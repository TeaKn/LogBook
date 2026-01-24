from bottle import route, run

@route('/')
def hello():
    return "Hi Tea, welcome to LogBook!"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)