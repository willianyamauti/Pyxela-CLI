import pandas as pd
import datetime as dt
from user import User
from graph import Graph
from pixel import Pixel


class Backend:
    """A class for the management of the application and its interactions with the json database"""

    credentials = {
        "username": "",
        "token": "",
        "graph_id": "",
        "graph_endpoint": "",
        "user_endpoint": "",
        "pixel_endpoint": "",
    }

    def __init__(self):
        """ Initialize the classes with empty arguments"""
        self.user = User()
        self.graph = Graph(self.credentials["token"], self.credentials["graph_endpoint"])
        self.pixel = Pixel(self.credentials["token"], self.credentials["graph_endpoint"])

    # ----------------------------------------------------------------------------------------------------------------------
    def create_new_user(self) -> None:
        """ Creates a new user with inputs"""
        is_user_created = False
        msg: str
        token = ""
        while not is_user_created:
            username = input("Username: ")
            msg, is_user_created, token = self.user.create_user(username)
            print(msg)
            msg, is_user_created, token = self.user.create_user(username)
        self.credentials["token"] = token
        url = self.user.create_user_url()
        self.credentials["user_endpoint"] = url

    # ----------------------------------------------------------------------------------------------------------------------
    def access_existing_user(self) -> None:
        """Access a existing user"""
        username = input("Username: ")
        token = input("Token: ")
        url = self.user.create_user_url()
        self.credentials["user_endpoint"] = url
        self.credentials["username"] = username
        self.credentials["token"] = token

    # ----------------------------------------------------------------------------------------------------------------------
    def fetch_user_info(self) -> str:
        """Fetch a user information"""
        credential = input("Type the desired info(username or token): ")
        try:
            info = self.user.fetch_access_credentials(credential)
            return info
        except KeyError:
            print(f"{credential} don't exist")

    # ----------------------------------------------------------------------------------------------------------------------
    def create_graph(self) -> tuple[bool, str]:
        """ Creates a new graph for the specified user"""
        token = ""
        user_endpoint = ""
        is_success = False

        # if the user atributes is already filled
        if self.credentials["username"] != "":
            token = self.credentials["token"]
            user_endpoint = self.credentials["user_endpoint"]
        # if no atribute is found
        else:
            self.access_existing_user()

        # sets the graph atributes
        self.graph.update_atributes(token=token, user_endpoint=user_endpoint)

        # ask for the inputs
        graph_config = self.__input_graph_parameters()

        # do the request to the API
        is_success, graph_id = self.graph.create_graph(*graph_config)
        # if the request is successful fetch the graph_endpoint
        if is_success:
            self.credentials["graph_endpoint"] = self.graph.create_graph_url()
        # return a tuple containing a boolean for the success and the graph id
        return is_success, graph_id

    def __input_graph_parameters(self) -> list[str]:
        """ Get the graph parameters input"""
        _graph_name = input(f"Type the graph name(ex: reading, cycling, studying, etc): ")
        _graph_unit = input(f"Type the unit used in the graph(ex: Km, days, hours, pages, etc): ")
        _graph_type = input(f"Choose between int(integers), float(decimals), type your choice: ")
        while _graph_type not in self.graph.TYPE:
            print(f"The type {_graph_type} is not supported!")
            _graph_type = input(f"Choose between int(integers), float(decimals), type your choice: ")
        _graph_color = input(f"Choose the desired color for the pixels (green, red, blue, yellow, purple or black):")
        while _graph_color not in self.graph.COLORS:
            print(f"The Color {_graph_color} is not supported!")
            _graph_type = input(f"Choose the desired color for the pixels (green, red, blue, yellow, purple or black):")

        return [_graph_name, _graph_unit, _graph_type, _graph_color]

    # ----------------------------------------------------------------------------------------------------------------------
    def manage_pixel(self):
        """Creates, updates and deletes a pixel according to the user input"""
        mode = self.__choose_pixel_mode()
        pixel_date, pixel_quantity = self.__input_pixel_parameters()
        is_success = self.pixel.manage_pixel(day=pixel_date, quantity=pixel_quantity, mode=mode)
        return is_success

    def __choose_pixel_mode(self) -> str:
        """get the input for the mode parameter for the pixel management"""
        option_is_invalid = True
        choice = ""
        options = {
            "1": 'create',
            "2": 'update',
            "3": 'delete',
        }

        while option_is_invalid:
            choice = input(f"Choose the desired option:\n1"
                           f"[1]Create pixel\n"
                           f"[2]Update pixel\n"
                           f"[3]Delete Pixel\n"
                           )

            try:
                if choice in options:
                    option_is_invalid = False
                    choice = options[choice]

            except KeyError as err:
                print("Invalid Option! Try again.")

        return options[choice]

    def __input_pixel_parameters(self) -> tuple[str, str]:
        options = {
            "1": dt.date.today(),
            "2": "",

        }
        option_is_invalid = True
        choice = ""
        pixel_date = ""
        while option_is_invalid:
            choice = input(f"Choose the desired option:\n1"
                           f"[1]Today\n"
                           f"[2]Custom date\n"
                           )
            try:
                if choice in options:
                    if choice == "1":
                        option_is_invalid = False
                        pixel_date = options[choice].strftime("%Y%m%d")
                    else:
                        option_is_invalid = False
                        year = int(input("Year (yyyy): "))
                        month = int(input("Month (mm): "))
                        day = int(input("Day (dd): "))
                        custom_date = dt.datetime(year=year, month=month, day=day)
                        pixel_date = custom_date.strftime("%Y%m%d")
            except KeyError as err:
                print("Invalid Option! Try again.")
        quantity = input("\nType the desired quantity to be add to the pixel: ")
        return pixel_date, quantity
