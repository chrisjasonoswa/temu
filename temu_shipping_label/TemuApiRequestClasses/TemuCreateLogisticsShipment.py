from dataclasses import dataclass, asdict, is_dataclass
from typing import Optional, List, TypedDict, Union
from dataclasses import field

from TemuApiRequestClasses import TemuApiCommonParams


@dataclass(kw_only=True)
class OrderSendInfo:
    # Required
    parentOrderSn: str
    orderSn: str
    quantity: int

    # Optional
    goodsId: Optional[int] = None
    skuId: Optional[int] = None

@dataclass(kw_only=True)
class SendSubRequest:
    # Required
    shipCompanyId: int
    warehouseId: str
    weight: str
    weightUnit: bool
    length: float
    width: float
    height: float
    dimensionUnit: str

    # Not Required
    extendWeight: Optional[float] = None
    extendWeightUnit: Optional[str] = None
    channelId: Optional[str] = None
    shipLogisticsType: Optional[str] = None
    signServiceId: Optional[int] = None
    confirmAcceptance: Optional[List[str]] = field(default_factory=list)


    def __post_init__(self):
        self.weight = f"{round(self.weight, 2):.2f}"
        self.length = f"{round(self.length, 2):.2f}"
        self.width = f"{round(self.width, 2):.2f}"
        self.height = f"{round(self.height, 2):.2f}"
        if self.extendWeight:
            self.extendWeight = f"{round(self.extendWeight, 2):.2f}"

@dataclass(kw_only=True)
class SendRequest:
    # Required
    shipCompanyId: int
    channelId: Optional[str]
    warehouseId: str
    weight: Union[str, float]
    weightUnit: bool
    length: Union[str, float]
    width: Union[str, float]
    height: Union[str, float]
    dimensionUnit: str

    # Not Required
    orderSendInfoList: Optional[List[OrderSendInfo]] = field(default_factory=list)
    extendWeight: Optional[Union[str, float]] = None
    extendWeightUnit: Optional[str] = None
    
    shipLogisticsType: Optional[str] = None
    pickupEndTime: Optional[int] = None
    pickupStartTime: Optional[int] = None
    splitSubPackage: Optional[bool] = None
    signServiceId: Optional[int] = None
    sendSubRequestList: Optional[List[SendSubRequest]] = field(default_factory=list)
    confirmAcceptance: Optional[List[str]] = field(default_factory=list)


    def __post_init__(self):
        self.weight = f"{round(self.weight)}"
        self.length = f"{round(self.length, 2):.2f}"
        self.width = f"{round(self.width, 2):.2f}"
        self.height = f"{round(self.height, 2):.2f}"
        if self.extendWeight:
            self.extendWeight = f"{round(self.extendWeight, 2):.2f}"


@dataclass(kw_only=True)
class TemuCreateLogisticsShipment(TemuApiCommonParams):
    sendType: int
    sendRequestList: List[SendRequest]
    shipLater: Optional[bool] = None
    shipLaterLimitTime: Optional[str] = None

    def __post_init__(self):
        super().__post_init__() 
        if not self.type:
            self.type="bg.logistics.shipment.create"

    def clean_dict(self, data=None):
        if data is None:
            data = asdict(self)

        if isinstance(data, list):
            return [self.clean_dict(item) for item in data if item is not None]
        elif isinstance(data, dict):
            return {
                key: self.clean_dict(value)
                for key, value in data.items()
                if value is not None
            }
        elif is_dataclass(data):
            return self.clean_dict(asdict(data))
        else:
            return data








