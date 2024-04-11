from app.services.number_to_english import NumberToEnglish

def test_negative_number_translation() -> None:
    response = NumberToEnglish().number_to_english(-20259191170198)
    expected_response = "negative twenty trillion two hundred fifty nine billion one hundred ninety one million one hundred seventy thousand one hundred ninety eight"
    assert response == expected_response
    
def test_positive_number_translation() -> None:
    response = NumberToEnglish().number_to_english(12345)
    expected_response = "twelve thousand three hundred forty five"
    assert response == expected_response