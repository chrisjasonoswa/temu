import time
import requests
import json
from bg_sign_generator_get import add_sign
from TemuApiRequestClasses import TemuGetShippingServicesParams


def get_temu_shipping_services(params: TemuGetShippingServicesParams):
    payload = {
        "access_token": params.access_token,
        "app_key": params.app_key,
        "timestamp": params.timestamp,
        "type": params.type,
        "warehouseId": params.warehouse_id,
        "length": f"{round(params.length, 2):.2f}",
        "width": f"{round(params.width, 2):.2f}",
        "dimensionUnit": params.dimension_unit,
        "weight": params.weight,
        "weightUnit": params.weight_unit,
        "height": f"{round(params.height, 2):.2f}",
    }

    # Optional parameters
    if params.extend_weight_unit is not None:
        payload["extendWeightUnit"] = params.extend_weight_unit
    if params.extend_weight is not None:
        payload["extendWeight"] = params.extend_weight
    if params.signature_on_delivery is not None:
        payload["signatureOnDelivery"] = params.signature_on_delivery
    if params.order_sn_list:
        payload["orderSnList"] = params.order_sn_list

    signed_payload = add_sign(payload, params.app_secret)

    print("Signed Payload:", json.dumps(signed_payload, indent=2))

    url = 'https://openapi-b-us.temu.com/openapi/router'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(signed_payload))
    return response.json()


# === 🧪 Run as standalone script ===
if __name__ == "__main__":
    shipping_params = TemuGetShippingServicesParams(
        app_key="4ebbc9190ae410443d65b4c2faca981f",
        app_secret="4782d2d827276688bf4758bed55dbdd4bbe79a79",
        access_token="uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",
        # extend_weight_unit="lb",
        warehouse_id="WH-04700686817432414",
        # extend_weight=10.0,
        length=10.00,
        width=5.0,
        dimension_unit="in",
        weight=10,
        # signature_on_delivery=False,
        order_sn_list=["211-19885516744230400"],
        weight_unit="lb",
        height=7.5,
    )

    result = get_temu_shipping_services(shipping_params)
    print("RESPONSE:", json.dumps(result, indent=2))
