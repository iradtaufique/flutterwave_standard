import math
import random
import requests


def process_payment(amount, name, email):
    hed = {'Authorization': 'Bearer ' + 'your secrete key'}
    data = {
        "tx_ref": '' + str(math.floor(1000000 + random.random() * 9000000)),
        "amount": amount,
        "currency": "RWF",
        "redirect_url": "http://localhost:8000/",
        # "redirect_url": myurl(request=request),
        "payment_options": "mobilemoneyrwanda",
        "meta": {
            "consumer_id": 23,
            "consumer_mac": "92a3-912ba-1192a"
        },
        "customer": {
            "email": email,
            "phonenumber": "0783845574",
            "name": name
        },
        "customizations": {
            "title": "Campany Name",
            "description": "Company Descriptions",
            "logo": "https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
        }
    }
    url = 'https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response = response.json()
    # print('==== meee ==============', myurl(request))
    print('=============== response==============', response)
    link = response['data']['link']
    return link