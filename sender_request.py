import requests
import configuration
import data


def post_create_order(body):
    return requests.post(configuration.URL + configuration.PATH_ORDER,
                         json=body)


response = post_create_order(data.order_body)
track_number = response.json()["track"]


def get_order():
    return requests.get(configuration.URL + configuration.PATH_TRACK, params={"t": track_number})


response = get_order()
body = response.json()
res_track = response.json()["order"]["track"]



