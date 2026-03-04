from datetime import datetime

import bottle
from model.dataClass.assessmentDataClass import AssessmentDataClass
from model.dataClass.subjectDataClass import SubjectDataClass

@bottle.get('/static/<datoteka:path>')
def static(datoteka):
    return bottle.static_file(datoteka, root='static')

"""
Calls:
- get all assessments that are coming up in the next month
"""
@bottle.get('/')
def dashboard():
    # Database initialization is done once in main.py at startup now.

    subject = SubjectDataClass.get_all_subjects()[0]

    month_days = 30

    assessments_serve = []
    assessments = AssessmentDataClass.get_current_assessments()
    for assessment in assessments:
        value = dict()
        days_until = (datetime.strptime(assessment.dueDate, '%Y-%m-%d %H:%M:%S.%f') - datetime.today()).days
        value['assessment'] = assessment.title + ' ' + assessment.subject.name
        value['days_until'] = days_until
        value['progress'] = (1 - days_until/month_days)*100
        assessments_serve.append(value)
    return bottle.template("dashboard", subject=subject, assessments=assessments_serve)


@bottle.get('/assessments')
def assessments():
    assessments_list = AssessmentDataClass.get_all_assessments()
    return bottle.template("assessments", assessments=assessments_list)

@bottle.post('/assessments/<assessment_id:int>')
def update_assessment(assessment_id):
    print("Called update assessment with id: ", assessment_id)
    data = bottle.request.json
    AssessmentDataClass.update_assessment(assessment_id, data)

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True, reloader=True)