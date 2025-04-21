
import time
import requests
import json
from bg_sign_generator_get import add_sign
from TemuApiRequestClasses import TemuGetWarehouseListParams

def get_temu_warehouse_list(params: TemuGetWarehouseListParams):
    payload = {
        "access_token": params.access_token,
        "app_key": params.app_key,
        "timestamp": params.timestamp,
        "type": "bg.order.list.v2.get"
    }
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

    result = get_temu_warehouse_list(
        TemuGetWarehouseListParams(
            app_key=app_key,
            app_secret=app_secret,
            access_token=access_token
        )
    )
    print("RESPONSE:", json.dumps(result, indent=2))
