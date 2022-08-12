import faker
import random


def create_fake_email():
    f = faker.Faker()
    return f.email()


def create_fake_password():
    password = ''
    password_length = 9
    for x in range(password_length):
        password += random.choice(list(
            '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return password
