from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import dataclass_json

from dataAccess.models.logModel import Log
from dataAccess.utilities import Entity
from model.dataClass.logTypeDataClass import LogTypeDataClass
from model.dataClass.assessmentDataClass import AssessmentDataClass


@dataclass_json
@dataclass
class LogDataClass(Entity):
    """
    Log entity class.
    """
    id: int = field(default=None)
    type: LogTypeDataClass = field(default=None)
    assessment: AssessmentDataClass = field(default=None)
    title: str = field(default=None)
    description: str = field(default=None)
    notes: str = field(default=None)
    createdOn: datetime = field(default=None)
    trackedFrom: datetime = field(default=None)
    trackedTo: datetime = field(default=None)

    NAME='title'

    def __post_init__(self):
        """
        Ensure that id and type are set to None if not provided. // todo: what is this description??
        """
        for k in ('id', 'type', 'assessment', 'title', 'description', 'notes', 'createdOn', 'trackedFrom', 'trackedTo'):
            if not getattr(self, k):
                setattr(self, k, None)

    @classmethod
    def get_all_logs(cls) -> list[dict]:
        rows = Log.list_all() # todo: implement list all
        print("Rows retrieved from Log.list_all():", rows)
        # have to convert the data to be able to use in javascript (None null problem)
        result = [{key: str(val) for key, val in r.items()} for r in rows]
        return result

    @classmethod
    def update_log(cls, log_id: int,  data: dict):
        """
        Update log with the provided data.
        :param log_id: ID of the log to update.
        :param data: Dictionary containing the updated assessment data.
        """
        data['log_id'] = log_id
        return Log.update_row(**data)

    @classmethod
    def get_total_study_time_by_subject(cls) -> list[dict]:
        return Log.list_total_time_by_subject()

    @classmethod
    def get_total_study_time_by_day(cls) -> list[dict]:
        return Log.list_total_time_by_day()


    @classmethod
    def create_log(cls, data: dict):
        """
        Create a new log with the provided data.
        :param data: Dictionary containing the new log data.
        """
        return Log.add_row(**data)

    def as_dict(self):
        return self.__dict__


