from core import config


def test_negative_number_translation(test_client) -> None:
    response = test_client.post(
        "/v1/numbers/num_to_english", json={"number": "-20259191170198"},
        headers={"token": str(config.API_KEY)},
    )
    expected_response = {
        "num_in_english": "negative twenty trillion two hundred fifty nine billion one hundred ninety one million one hundred seventy thousand one hundred ninety eight",
        "status": "ok"
    }
    assert response.status_code == 201
    assert response.json() == expected_response


def test_no_payload_provided(test_client) -> None:
    response = test_client.post(
        "/v1/numbers/num_to_english", json={}, headers={"token": str(config.API_KEY)})
    assert response.status_code == 422


def test_positive_number_translation(test_client) -> None:
    response = test_client.post(
        "/v1/numbers/num_to_english", json={"number": "12345"}, headers={"token": str(config.API_KEY)}
    )
    expected_response = {
        "num_in_english": "twelve thousand three hundred forty five",
        "status": "ok"
    }
    assert response.status_code == 201
    assert response.json() == expected_response


def test_zero_translation(test_client) -> None:
    response = test_client.post(
        "/v1/numbers/num_to_english", json={"number": "0"}, headers={"token": str(config.API_KEY)},
    )
    expected_response = {
        "num_in_english": "zero",
        "status": "ok"
    }
    assert response.status_code == 201
    assert response.json() == expected_response


def test_invalid_input_type(test_client) -> None:
    response = test_client.post(
        "/v1/numbers/num_to_english", json={"number": "not_a_number"}, headers={"token": str(config.API_KEY)},
    )
    assert response.status_code == 422


def test_missing_field_in_payload(test_client) -> None:
    response = test_client.post("/v1/numbers/num_to_english",
                                json={"not_number": "123"}, headers={"token": str(config.API_KEY)},)
    assert response.status_code == 422
