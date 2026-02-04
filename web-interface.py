from datetime import date

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

    # assessment countdown
    # npr en mesec pred assessmentom želim objavit countdown
    # lahko se doda v subjectDataClass in potem se izpiše tukaj
    # tukaj samo pride data - st dni do assessmenta
    month = 30
    today = date.today()
    pisni_izpit_pb1 = date(2026, 2, 13)
    days_until: int = (pisni_izpit_pb1 - today).days
    progress = (1 - (days_until / month)) * 100
    print("Progress: ", progress)
    assessment = "Pisni izpit Podatkovne baze 1"
    return dict(subject=subject, assessment = assessment, days_until=days_until, progress=progress)

@bottle.get('/subject')
@bottle.view('logs.html')
def logs():
    subject = SubjectDataClass.create_subject('New Subject')
    print(subject)
    return dict()

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True, reloader=True)