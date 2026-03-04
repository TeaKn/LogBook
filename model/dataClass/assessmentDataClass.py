from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import dataclass_json

from dataAccess.models.assessmentModel import Assessment
from dataAccess.utilities import Entity
from model.dataClass.assessmentTypeDataClass import AssessmentTypeDataClass
from model.dataClass.subjectDataClass import SubjectDataClass


@dataclass_json
@dataclass
class AssessmentDataClass(Entity):
    """
    Assessment entity class.
    """
    id: int = field(default=None)
    subject: SubjectDataClass = field(default=None)
    type: AssessmentTypeDataClass = field(default=None)
    title: str = field(default=None)
    createdOn: datetime = field(default=None)
    dueDate: datetime = field(default=None)
    doneOn: datetime = field(default=None)
    grade: int = field(default=None)

    NAME='title'

    def __post_init__(self):
        """
        Ensure that id and value are set to None if not provided.
        """
        for k in ('id', 'subject', 'type', 'title', 'createdOn', 'dueDate', 'doneOn', 'grade'):
            if not getattr(self, k):
                setattr(self, k, None)

    @classmethod
    def get_current_assessments(cls) -> list['AssessmentDataClass']:
        """
        Call the model's class-level list method and convert each row/object
        into an AssessmentDataClass instance.
        Here the parameter for number of days is passed.
        """
        rows = Assessment.list_assessments_due_within(days=30)
        print("Rows retrieved from Assessment.list_assessments_due_within():", rows)
        result = []
        for r in rows:
            result.append(
                cls(id=r.get('id'),
                    subject=SubjectDataClass(name=r.get('subject_name')),
                    type=AssessmentTypeDataClass(value=r.get('type')),
                    title=r.get('title'),
                    dueDate=r.get('dueDate')
                    )
            )
        print("Result ", result)
        return result

    @classmethod
    def get_all_assessments(cls) -> list[dict]:
        rows = Assessment.list_all()
        print("Rows retrieved from Assessment.list_all():", rows)
        # have to convert the data to be able to use in javascript (None null problem)
        result = [{key: str(val) for key, val in r.items()} for r in rows]
        return result

    @classmethod
    def update_assessment(cls, assessment_id: int,  data: dict):
        """
        Update an assessment with the provided data.
        :param assessment_id: ID of the assessment to update.
        :param data: Dictionary containing the updated assessment data.
        """
        data['assessment_id'] = assessment_id
        return Assessment.update_row(**data)

    def as_dict(self):
        return self.__dict__


