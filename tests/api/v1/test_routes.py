import json
from flask import url_for


def test_get_incomes(client, session):
    response = client.get(url_for('api.v1.get_incomes'))
    assert len(response.json) == 0

    income = {
        'amount': 100,
        'description': 'test income'
    }

    client.post(url_for('api.v1.add_income'), data=json.dumps(income), content_type='application/json')
    response = client.get(url_for('api.v1.get_incomes'))

    assert len(response.json) == 1