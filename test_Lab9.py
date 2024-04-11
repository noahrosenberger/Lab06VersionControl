def encoder(password):
    result = ""
    for i in password:
        number = int(i)
        result += str(number+3)
    return result


def decoder(password):
    decoded_password = ""
    for digit in password:
        decoded_digit = (int(digit) - 3) % 10
        decoded_password += str(decoded_digit)
    return decoded_password

def main():
    pass