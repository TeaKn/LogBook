from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from dataAccess.models.subjectModel import Subject
from dataAccess.utilities import Entity

@dataclass_json
@dataclass
class SubjectDataClass(Entity):
    """
    Subject entity class.
    """
    id: int = field(default=None)
    name: str = field(default=None)

    NAME='name'

    def __post_init__(self):
        """
        Ensure that id and name are set to None if not provided.
        """
        for k in ('id', 'name'):
            if not getattr(self, k):
                setattr(self, k, None)

    @classmethod
    def get_all_subjects(cls) -> list['SubjectDataClass']:
        """
        Call the model's class-level list method and convert each row/object
        into a SubjectDataClass instance.
        """
        rows = Subject.list_all()  # use class method, not Subject()
        print('Iščem vse predmete:', rows)
        result = []
        for r in rows:
            if isinstance(r, dict):
                print('r je dict:', r)
                result.append(cls(id=r.get('id'), name=r.get('name')))
            else:
                print('r je objekt:', r)
                result.append(cls(id=getattr(r, 'id', None), name=getattr(r, 'name', None)))
        print(result)
        return result

    @classmethod
    def create_subject(cls, name: str) -> int:
        """
        Create a subject via the model API. Prefer calling the model class method
        if available.
        """
        if hasattr(Subject, 'add_row'):
            return Subject.add_row(name=name)
        # fallback to instance method if model uses instance API
        s = Subject()
        s.name = name
        return s.add_row(name=s.name)


