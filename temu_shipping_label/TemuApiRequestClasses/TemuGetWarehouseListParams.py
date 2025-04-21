from dataclasses import dataclass, asdict
import time
from typing import Optional, List, Union
from TemuApiRequestClasses import TemuApiCommonParams


@dataclass(kw_only=True)
class TemuGetWarehouseListParams(TemuApiCommonParams):
    def __post_init__(self):
        super().__post_init__() 
        if not self.type:
            self.type="bg.logistics.warehouse.list.get"