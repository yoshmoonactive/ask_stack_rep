import json


def test_simple_prediction(app, client):
    res = client.post('/predict', data=json.dumps(
        {"some_data": "0"}))
    assert res.status_code == 200
    expected = {'500'}
    assert expected == json.loads(res.get_data(as_text=True))
