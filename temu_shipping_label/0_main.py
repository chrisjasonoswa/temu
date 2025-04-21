
from bg_1_1_logistics_warehouse_list_get import get_temu_warehouse_list
from bg_1_2_logistics_shippingservices_get import get_temu_shipping_services
import json
from TemuApiRequestClasses import TemuGetShippingServicesParams, TemuGetWarehouseListParams


def get_temu_shipping_label():
    app_key = "4ebbc9190ae410443d65b4c2faca981f"
    app_secret = "4782d2d827276688bf4758bed55dbdd4bbe79a79"
    access_token = "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7"

    #1.Determine the composition of the package and query recommended logistics channels:
    #    1.1 Use bg.logistics.warehouse.list.getto query the warehouse available for shipping in the store.
    get_temu_warehouse_list_response = get_temu_warehouse_list(
        TemuGetWarehouseListParams(
            app_key=app_key,
            app_secret=app_secret,
            access_token=access_token
        )
    )
    warehouse_list = get_temu_warehouse_list_response["result"]["warehouseList"]
    first_warehouse = warehouse_list[0]
    print("Warehouse List:", json.dumps(warehouse_list, indent=2), "\n")

    #    1.2 Use bg.logistics.shippingservices.get to query the recommended logistics channels.
    get_temu_shipping_services_response = get_temu_shipping_services(
        TemuGetShippingServicesParams(
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
    )

    print("Shipping Services:", json.dumps(get_temu_shipping_services_response, indent=2))

if __name__ == "__main__":
    get_temu_shipping_label()
