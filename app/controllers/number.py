from app.services import NumberToEnglish


class NumberController:
    def __init__(self):
        self.number_service = NumberToEnglish()

    async def convert_to_english(self, number: str):
        """
        Converts a given number to its English representation.

        Args:
            number (str): The number to be converted.

        Returns:
            dict: A dictionary containing the status and the number in English representation.
                If the conversion is successful, the dictionary will have the following structure:
                {"status": "ok", "num_in_english": <english_number>}
                If an exception occurs during the conversion, the dictionary will have the following structure:
                {"status": <exception_message>}

        Raises:
            ValueError: If the input number is not a valid integer.

        """
        try:
            english_number = self.number_service.number_to_english(int(number))
            return {"status": "ok", "num_in_english": english_number}
        except ValueError as ve:
            return {"status": str(ve)}
        except Exception as e:
            return {"status": str(e)}
