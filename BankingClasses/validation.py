class Validation:
    """ This class contains methods for validating email addresses and passwords."""

    @staticmethod
    def validate_email(email):
        """
        Validates an email address.

        Args:
          email (str): The email address to validate.

        Returns:
          bool: True if the email contains an '@' symbol, False otherwise.
        """
        return "@" in email

    @staticmethod
    def validate_password(password):
        """
        Validates a password based on the following criteria:
        - The password must be at least 8 characters long.
        - The password must contain at least one uppercase letter,
          one lowercase letter, one digit, and one special character (!@#$%^&*).

        Args:
          password (str): The password to validate.

        Returns:
          bool: True if the password meets all criteria, False otherwise.
        """
        if len(password) < 8:
            return False

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_characters = "!@#$%^&*"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_characters:
                has_special = True

        return has_upper and has_lower and has_digit and has_special
