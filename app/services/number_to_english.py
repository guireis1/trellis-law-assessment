import logging

class NumberToEnglish:
    """
    A class for converting numbers to their English word representation.
    """

    def __init__(self):
        """
        Initializes the class with lists for ones, tens, and powers of 10.
        """
        self.ones = [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ]
        self.tens = [
            "",
            "",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ]
        self.powers_of_10 = [
            "",
            "thousand",
            "million",
            "billion",
            "trillion",
            "quadrillion",
            "quintillion",
            "sextillion",
            "septillion",
            "octillion",
            "nonillion",
            "decillion",
        ]

        # Configure logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def number_to_english(self, number: int) -> str:
        """
        Converts a number to its English word representation.

        Args:
            number (int): The number to convert.

        Returns:
            str: The English word representation of the number.
        """
        self.logger.info(f"Converting number: {number}")

        if number == 0:
            return self.ones[0]
        elif number < 0:
            self.logger.warning("Negative number provided")

            return "negative " + self.number_to_english(abs(number))

        digits = [int(d) for d in str(number)]
        groups = [
            digits[max(0, len(digits) - 3 * (i + 1)) : len(digits) - 3 * i]
            for i in range((len(digits) + 2) // 3)
        ]

        group_words = []
        for i, group in enumerate(groups):
            if group:
                group_words.append(
                    self._number_to_english_group(group) + " " + self.powers_of_10[i]
                )

        result = " ".join(group_words[::-1]).strip()
        self.logger.info(f"Result: {result}")

        return result

    def _number_to_english_group(self, group: list) -> str:
        """
        Converts a group of up to three digits to English words.

        Args:
            group (list): A list of up to three digits.

        Returns:
            str: The English word representation of the group.
        """
        group = [0] * (3 - len(group)) + group
        hundreds, tens, ones = group
        words = []

        if hundreds:
            words.append(self.ones[hundreds] + " hundred")

        if tens or ones:
            if tens < 2:
                words.append(self.ones[tens * 10 + ones])
            else:
                words.append(self.tens[tens])
                if ones:
                    words.append(self.ones[ones])

        return " ".join(words)
