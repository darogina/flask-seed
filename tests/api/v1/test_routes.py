import json

from flask import url_for


def test_get_incomes(client):
    _incomes_url = url_for('api.v1.incomes')

    # Make sure db is empty
    response = client.get(_incomes_url)
    assert len(response.json) == 0

    # Create income
    income = {
        'amount': 100,
        'description': 'test income'
    }
    client.post(_incomes_url, data=json.dumps(income), content_type='application/json')

    # Get incomes and assert only one exists
    response = client.get(_incomes_url)
    assert len(response.json) == 1
