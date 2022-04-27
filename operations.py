import requests

login_data = {
    "username": "admin",
    "password": "password123"
}


def get_token(data):
    return (requests.post("https://restful-booker.herokuapp.com/auth", json=data)).json()['token']


def create_user(data):
    return requests.post("https://restful-booker.herokuapp.com/booking", json=data)


def get_users():
    return requests.get("https://restful-booker.herokuapp.com/booking")


def get_user(booking_id):
    return requests.get("https://restful-booker.herokuapp.com/booking/{:d}".format(booking_id))


def update_user_patch(data, booking_id):
    return requests.patch("https://restful-booker.herokuapp.com/booking/{:d}".format(booking_id), json=data,
                          cookies={"token": get_token(login_data)})


def update_user_put(data, booking_id):
    return requests.put("https://restful-booker.herokuapp.com/booking/{:d}".format(booking_id), json=data,
                        cookies={"token": get_token(login_data)})


def delete_user(booking_id):
    return requests.delete("https://restful-booker.herokuapp.com/booking/{:d}".format(booking_id),
                           cookies={"token": get_token(login_data)})
