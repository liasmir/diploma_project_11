# Наталья Смирнова, 5-я когорта - 11 спринт. Инженер по тестированию плюс
import data
import sender_request


def test_request_order_by_track():
    sender_request.post_create_order(data.order_body) # создание заказа
    resp = sender_request.get_order() # получение заказа по треку
    assert sender_request.track_number == sender_request.res_track # проверка, что трек созданного заказа соответствует треку полученного заказа.
    actual_st_code = resp.status_code
    expected_st_code = 200
    assert actual_st_code == expected_st_code, \
        f"Expected{expected_st_code}, Actual{actual_st_code}"

