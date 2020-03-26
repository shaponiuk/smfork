JOHNS_CREDENTIALS = {
    'username': 'John',
    'password': 'secret',
}

JOHN = {
    **JOHNS_CREDENTIALS,
    'email': 'john@example.com',
    'birth_date': '2020-02-06',
    'gender': 'M',
    'description': 'abc',
    'phone_number': '999999999',
}

JOHNS_RUNNING = {
    'level': 0,
    'sport': 1
}

MIM_COORDINATES = [
    52.211769,
    20.982064
]

MIM_WORKOUT = {
    'name': 'MIM',
    'max_people': 10,
    'desired_proficiency': 0,
    'location': {
        'type': 'Point',
        'coordinates': MIM_COORDINATES,
    },
    'location_name': 'mim',
    'level': 9,
    'start_time': '2020-10-10T01:01:00Z',
    'end_time': '2020-10-10T01:01:00Z',
    'description': 'abc',
    'age_min': 0,
    'age_max': 90,
    'sport': 1,
    'expected_gender': 'E',
}

BITWY_WARSZAWSKIEJ_COORDINATES = [
    52.211858,
    20.977279
]

BITWY_WARSZAWSKIEJ_WORKOUT = {
    'name': 'Bitwy Warszawskiej',
    'max_people': 10,
    'desired_proficiency': 0,
    'location': {
        'type': 'Point',
        'coordinates': BITWY_WARSZAWSKIEJ_COORDINATES,
    },
    'location_name': 'bw',
    'level': 9,
    'start_time': '2020-10-10T01:01:00Z',
    'end_time': '2020-10-10T01:01:00Z',
    'description': 'abc',
    'age_min': 0,
    'age_max': 90,
    'sport': 1,
    'expected_gender': 'E',
}

