import requests
import json
from nested_lookup import nested_lookup, nested_update, nested_delete


def check_status_code(url, res):
    if res.status_code == 200:
        print(f'resp.status_code == 200 for {url} => OK')
    elif res.status_code == 201:
        print(f'resp.status_code == 201 for {url} => OK')
    elif res.status_code == 204:
        print(f'resp.status_code == 204 for {url} => OK')
    else:
        print(f'Actual resp.status_code is "{res.status_code}", "{res.text}"'
              f'\nfor url: {url} => error')


def get_response(url):
    res_status = requests.get(url, headers=header, verify=header)
    res_objects = json.loads(res_status.text)
    check_status_code(url, res_status)

    return res_status, res_objects


def get_apartment_owner_id(url, number):
    full_url = f'{url}/?__all__'
    res_status, res_objects = get_response(full_url)

    # print(f'res_status is: {res_status}')
    # print(f'res_object is: {json.dumps(res_objects, indent=4, sort_keys=True)}')

    if number in nested_lookup(key='car_number', document=res_objects) or \
            number in nested_lookup(key='motorcycle_number', document=res_objects):
        print()

    apartment_owner_id = None
    for res_object in res_objects:
        for i in res_object['rn_cars']:
            if number == i['car_number_id']['car_number']:
                apartment_owner_id = res_object['rn_apartments'][0]['apartment_owner_id']

        for i in res_object['rn_motorcycles']:
            if number == i['motorcycle_number_id']['motorcycle_number']:
                apartment_owner_id = res_object['rn_apartments'][0]['apartment_owner_id']

    return apartment_owner_id


def in_out_parking_count(url, plus_minus):
    res_status, res_objects = get_response(url)

    # print(f'res_status is: {res_status}')
    # print(f'res_object is: {json.dumps(res_objects, indent=4, sort_keys=True)}')

    if plus_minus == 'IN' and res_objects[0]['parking_count'] < res_objects[0]['get_amount_of_parking']:
        print('Open gate')

        print('parking_count +1')
        data = {'parking_count': res_objects[0]['parking_count'] + 1}
        res = requests.put(f'{url}', data=data, headers=header)
        check_status_code(url, res)
    elif plus_minus == 'OUT':
        if res_objects[0]['parking_count'] > 0:
            print('parking_count -1')
            data = {'parking_count': res_objects[0]['parking_count'] - 1}
            res = requests.put(f'{url}', data=data, headers=header)
            check_status_code(url, res)
        else:
            print('All cars already out')
    else:
        print('Call to guard')


def get_number():
    # return 'IN', '33333'
    return 'OUT', '33333'


def main():
    while True:
        try:
            input_type, number = get_number()
            apartment_owner_id = get_apartment_owner_id(f'{main_url}/ApartmentOwnerApp', number)
            if apartment_owner_id:
                in_out_parking_count(f'{main_url}/ApartmentNumberApp/{apartment_owner_id}/', input_type)
            else:
                print('There is no apartment_owner_id')
        except Exception as err:
            print('Have some error - need call to guard ')
            print(err)

        print()


if __name__ == '__main__':
    main_url = r'http://asil-azaguri2:8000'
    api_token = r'Token e87186f7ba0c4249e596ef212d836f6e5e329b8a'
    header = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': api_token}

    main()
