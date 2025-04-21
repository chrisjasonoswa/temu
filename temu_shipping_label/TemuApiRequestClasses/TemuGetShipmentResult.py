from dataclasses import dataclass, asdict, field
from typing import List
from TemuApiRequestClasses import TemuApiCommonParams


@dataclass(kw_only=True)
class TemuGetShipmentResult(TemuApiCommonParams):
    packageSnList: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        super().__post_init__() 
        if not self.type:
            self.type="bg.logistics.shipment.result.get"