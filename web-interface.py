import bottle
from model.dataClass.subjectDataClass import SubjectDataClass
from dataAccess.db import initialize_db


@bottle.get('/static/<datoteka:path>')
def static(datoteka):
    return bottle.static_file(datoteka, root='static')

@bottle.get('/')
@bottle.view('index.html')
def index():
    initialize_db()
    subject = SubjectDataClass.get_all_subjects()[0]
    return dict(subject=subject)

@bottle.get('/subject')
@bottle.view('logs.html')
def logs():
    subject = SubjectDataClass.create_subject('New Subject')
    print(subject)
    return dict()

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True, reloader=True)