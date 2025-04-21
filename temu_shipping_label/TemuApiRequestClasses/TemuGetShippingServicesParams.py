from dataclasses import dataclass, asdict, is_dataclass
from typing import Optional, List, Union
from TemuApiRequestClasses import TemuApiCommonParams


@dataclass(kw_only=True)
class TemuGetShippingServicesParams(TemuApiCommonParams):
    # API Specific Parameters
    warehouse_id: str
    length: float
    width: float
    dimension_unit: str
    weight: int
    weight_unit: str
    height: float

    # Optional Fields
    extend_weight_unit: Optional[str] = None
    extend_weight: Optional[str] = None
    signature_on_delivery: Optional[bool] = None
    order_sn_list: Optional[List[str]] = None

    def __post_init__(self):
        super().__post_init__() 
        if not self.type:
            self.type="bg.logistics.shippingservices.get"