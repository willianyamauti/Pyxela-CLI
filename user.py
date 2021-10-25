import requests
from random import randint, choice, shuffle
import string

# my token = VdV1qI5V3V7-Cg$|
# my username = willianyamauti

pixela_endpoint = "https://pixe.la/v1/users"


class User:
    params = {
        'token': '',
        'username': '',
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes',
    }

    @staticmethod
    def __generate_token():
        """ generates a random token from the pixela specifications"""
        random_symbols = [choice(string.punctuation) for _ in range(randint(2, 4))]
        random_letters = [choice(string.ascii_letters) for _ in range(randint(8, 10))]
        random_numbers = [choice(string.digits) for _ in range(randint(2, 4))]

        token_list = random_symbols + random_letters + random_numbers
        shuffle(token_list)
        token = "".join(token_list)
        print(token)
        return token

    def create_user(self, username: str) -> tuple[str, bool, str]:
        """
         Creates a new user at pixela, returns a tuple with the token, request results and the message returned
         by the API.\n
         msg: a string containing the success msg or an error msg specifying what caused the request to fail.\n
         is_success: a boolean for verification, if False you may want to try creating the user again.
         token: returns the token
         """
        self.params['username'] = username
        token = self.__generate_token()
        self.params['token'] = token
        response = requests.post(url=pixela_endpoint, json=self.params)
        log = response.json()
        msg, is_success = log.values()
        return msg, is_success, token

    def input_access_credentials(self, username: str, token: str):
        """ Access a existing user."""
        self.params['token'] = token
        self.params['username'] = username

    def fetch_access_credentials(self, credential: str) -> str:
        """fetch the specified credential from the user"""
        return self.params.get(credential)

    def create_user_url(self) -> str:
        """create the user url, based on the user parameters"""
        return f"https://pixe.la/v1/users/{self.params['username']}"


# user = User()
# user.create_user("teste1")
# print("Save your token: " + user.params["token"])
# url = user.create_user_url()
# print(url)