
from dataclasses import asdict
import time
from typing import List
import requests
import json
from bg_sign_generator_get import add_sign
from TemuApiRequestClasses import (
    TemuCreateLogisticsShipment,
    OrderSendInfo,
    SendRequest,
    SendSubRequest,
)

def clean_dict(data):
    if isinstance(data, dict):
        return {
            key: clean_dict(value)
            for key, value in data.items()
            if value not in [None, [], ""]
        }
    elif isinstance(data, list):
        return [clean_dict(item) for item in data if item not in [None, [], ""]]
    else:
        return data

def create_logistics_shipment(params: TemuCreateLogisticsShipment):
    payload = {
        "access_token": params.access_token,
        "app_key": params.app_key,
        "timestamp": params.timestamp,
        "type": params.type,
        "sendType": params.sendType,
        "shipLater": params.shipLater,
        # "shipLaterLimitTime": params.shipLaterLimitTime,
        "sendRequestList": [
            clean_dict(asdict(item)) for item in params.sendRequestList
        ]  # Serialize custom classes here and clean empty values
    }
    print("payload:", json.dumps(payload, indent=2))
    
    signed_payload = add_sign(payload, params.app_secret)
    url = 'https://openapi-b-us.temu.com/openapi/router'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(signed_payload))
    return response.json()

# === 🧪 Run as standalone script ===
if __name__ == "__main__":
    app_key = "4ebbc9190ae410443d65b4c2faca981f"
    app_secret = "4782d2d827276688bf4758bed55dbdd4bbe79a79"
    access_token = "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7"
    send_type = 1
    order_send_info_list: List[OrderSendInfo] = [
        OrderSendInfo(
            parentOrderSn="PO-211-19885453829670400",
            orderSn="211-19885521987110400",
            quantity=1
        )
    ]

    send_request_list = [
        SendRequest(
            shipCompanyId = 732613859,
            channelId = 841290702659608576,
            warehouseId = "WH-04700686817432414",
            weight = 10,
            weightUnit = "lb",
            length = 10,
            width = 5,
            height = 7.5,
            dimensionUnit = "in",
            orderSendInfoList = order_send_info_list
        )
    ]

    
    params = TemuCreateLogisticsShipment(
        app_key=app_key,
        app_secret=app_secret,
        access_token=access_token,
        sendType=1,
        sendRequestList=send_request_list,
        shipLater=True,
        shipLaterLimitTime="96",
    )
    result = create_logistics_shipment(params)
    print("RESPONSE:", json.dumps(result, indent=2))
    