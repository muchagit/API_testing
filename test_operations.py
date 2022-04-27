import operations
import unittest
import jsonpath

data = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

update_data_put = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

update_data_patch = {
    "firstname": "James",
    "lastname": "Brown"
}


class Test_TestValue(unittest.TestCase):

    def test_get_users(self):
        resp = operations.get_users()
        self.assertEqual(resp.status_code, 200)

    def test_create_user(self):
        resp = operations.create_user(data)
        self.assertEqual(resp.status_code, 200)

    def test_get_user(self):
        new_user = operations.create_user(data)
        booking_id = jsonpath.jsonpath(new_user.json(), 'bookingid')
        resp = operations.get_user(booking_id[0])
        self.assertEqual(resp.status_code, 200)

    def test_update_user_put(self):
        new_user = operations.create_user(data)
        booking_id = jsonpath.jsonpath(new_user.json(), 'bookingid')
        resp = operations.update_user_put(update_data_put, booking_id[0])
        self.assertEqual(resp.status_code, 200)

    def test_update_user_patch(self):
        new_user = operations.create_user(data)
        booking_id = jsonpath.jsonpath(new_user.json(), 'bookingid')
        resp = operations.update_user_patch(update_data_patch, booking_id[0])
        self.assertEqual(resp.status_code, 200)

    def test_delete_user(self):
        new_user = operations.create_user(data)
        booking_id = jsonpath.jsonpath(new_user.json(), 'bookingid')
        resp = operations.delete_user(booking_id[0])
        self.assertEqual(resp.status_code, 201)
