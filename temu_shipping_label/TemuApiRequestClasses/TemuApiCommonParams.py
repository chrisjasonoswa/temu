from dataclasses import dataclass, asdict
import time
from typing import Optional, List, Union

@dataclass(kw_only=True)
class TemuApiCommonParams:
    # Common Parameters
    app_key: str
    app_secret: str
    access_token: str

    # Common Parameters but just define this in the child classes
    timestamp: Optional[str] = None
    type: Optional[str] = None

    # Optional Fields
    data_type: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = str(int(time.time()))