import random
import string


def generate_secure_password(num_small, num_caps, num_digits, num_special):
    """
    Generate a secure password based on the specified parameters.

    Parameters:
    - num_small: Number of lowercase letters in the password
    - num_caps: Number of uppercase letters in the password
    - num_digits: Number of digits in the password
    - num_special: Number of special characters in the password

    Returns:
    - A randomly generated secure password
    """
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Initialize password string
    password = ''

    # Generate lowercase letters
    password += ''.join(random.choices(lowercase_letters, k=num_small))

    # Generate uppercase letters
    password += ''.join(random.choices(uppercase_letters, k=num_caps))

    # Generate digits
    password += ''.join(random.choices(digits, k=num_digits))

    # Generate special characters
    password += ''.join(random.choices(special_characters, k=num_special))

    # Shuffle the password characters
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


# Example usage
secure_password = generate_secure_password(4, 3, 2, 1)
print("Generated Password:", secure_password)