from passlib.hash import pbkdf2_sha512
import re


class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w\.-]+@([\w]+\.)+[\w]+$')
        if email_address_matcher.match(email):
            return True
        else:
            return False

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)
