from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from dataAccess.utilities import Entity

@dataclass_json
@dataclass
class AssessmentTypeDataClass(Entity):
    """
    Assessment type entity class.
    """
    id: int = field(default=None)
    value: str = field(default=None)

    NAME='value'

    def __post_init__(self):
        """
        Ensure that id and value are set to None if not provided.
        """
        for k in ('id', 'value'):
            if not getattr(self, k):
                setattr(self, k, None)


