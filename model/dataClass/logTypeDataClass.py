from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from dataAccess.utilities import Entity

@dataclass_json
@dataclass
class LogTypeDataClass(Entity):
    """
    Log type entity class.
    """
    id: int = field(default=None)
    type: str = field(default=None)

    NAME='type'

    def __post_init__(self):
        """
        Ensure that id and type are set to None if not provided.
        """
        for k in ('id', 'type'):
            if not getattr(self, k):
                setattr(self, k, None)


