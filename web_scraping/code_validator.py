# code_validator.py
import re

MIN_CODE_LENGTH = 8
MAX_CODE_LENGTH = 15

class CodeValidator:
    @staticmethod
    def extract_and_validate(text):
        codes = set()
        potential_codes = re.findall(rf'\b[A-Z0-9]{{{MIN_CODE_LENGTH},{MAX_CODE_LENGTH}}}\b', text)
        for code in potential_codes:
            if code.isalnum() and code.isupper():
                codes.add(code)
        return codes