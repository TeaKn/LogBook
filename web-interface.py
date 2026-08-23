from datetime import datetime

import bottle
from model.dataClass.assessmentDataClass import AssessmentDataClass
from model.dataClass.logDataClass import LogDataClass
from model.dataClass.subjectDataClass import SubjectDataClass
from bottle import response, app
from bottle_cors_plugin import cors_plugin

DAYS : int = 30

@bottle.get('/subjects')
def subjects():
    subjects_list = SubjectDataClass.get_all_subjects()
    return {'subjects': subjects_list}

@bottle.get('/assessments')
def assessments():
    assessments_list = AssessmentDataClass.get_all_assessments()
    return {'assessments': assessments_list}

@bottle.get('/assessments/current')
def current_assessments():
    assessments_serve = []
    assessments = AssessmentDataClass.get_current_assessments()
    for assessment in assessments:
        value = dict()
        days_until = (assessment.dueDate.date() - datetime.today().date()).days + 1
        value['assessment'] = assessment.title + ' ' + assessment.subject.name
        value['days_until'] = days_until
        value['progress'] = (1 - days_until / DAYS) * 100
        assessments_serve.append(value)
    return {'assessments': assessments_serve}

@bottle.post('/assessments/<assessment_id:int>')
def update_assessment(assessment_id):
    print("Called update assessment with id: ", assessment_id)
    data = bottle.request.json
    AssessmentDataClass.update_assessment(assessment_id, data)

@bottle.post('/assessments')
def create_assessment():
    print("Called create assessment")
    data = bottle.request.json
    AssessmentDataClass.create_assessment(data)


@bottle.post('/logs')
def create_log():
    print("Called create log")
    data = bottle.request.json
    LogDataClass.create_log(data)

@bottle.get('/logs')
def list_logs():
    limit = bottle.request.query.get('limit', type=int)
    print("Limit:", limit)

    print("Called list logs.")
    data = LogDataClass.get_logs(limit)
    return {'logs': data}

@bottle.get('/logs/current')
def get_current_log():
    data = LogDataClass.get_last_current_log()
    print("Called current log... ")
    return data

@bottle.get('/statistics/study-time-by-subject')
def get_study_times_by_subject():
    """
    List all total study time by subject.
    """
    data = LogDataClass.get_total_study_time_by_subject()
    return {'subjects': data}

@bottle.get('/statistics/study-time-by-day')
def get_study_times_by_subject():
    """
    List all total study time by day.
    """
    data = LogDataClass.get_total_study_time_by_day()
    return {'days': data}

@bottle.get('/statistics/assessment-by-type')
def get_assessments_by_type():
    """
    Aggregate assessment by type for subject.
    """
    data = AssessmentDataClass.get_assessment_count_for_subject_by_type()
    return {'assessments': data}

app = app()
app.install(cors_plugin('*'))

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True, reloader=True)
    response.content_type = 'application/json'
