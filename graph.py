import requests
from random import choice, shuffle
import string

pixela_endpoint = "https://pixe.la/v1/users"

TYPE = ('int', 'float')
COLORS = {'green': 'shibafu', 'red': 'momiji', 'blue': 'sora', 'yellow': 'ichou', 'purple': 'ajisai', 'black': 'kuro', }


# username = "willianyamauti"
# token = "VdV1qI5V3V7-Cg$|"


class Graph:
    """ The Graph class is used for the management of a  pixela graph.\n
        The class requires a Token and a endpoint to make modifications.
    """

    TYPE = ('int', 'float')
    COLORS = {'green': 'shibafu', 'red': 'momiji', 'blue': 'sora', 'yellow': 'ichou', 'purple': 'ajisai',
              'black': 'kuro', }

    graph_config = {
        'id': '',
        'name': '',
        'unit': '',
        'type': '',
        'color': '',
    }

    headers = {
        "X-USER-TOKEN": '',
    }

    def __init__(self, token: str, user_endpoint: str):
        self.headers["X-USER-TOKEN"] = token
        self.graph_endpoint = f"{user_endpoint}/graphs"

    @staticmethod
    def generate_id():
        """
        Generates a random id, used to create new graphs
        """
        random_letters = [choice(string.ascii_lowercase) for _ in range(5)]
        random_numbers = [choice(string.digits) for _ in range(4)]
        id_list = random_letters + random_numbers
        shuffle(id_list)
        new_id = choice(random_letters)
        new_id += "".join(id_list)
        print("Your id is :", new_id)
        return new_id

    def create_graph(self, _graph_name: str, _graph_unit: str, _graph_type: str, _graph_color: str):
        """
            Creates a new Graph in the Pixela Api using the request module.
        """
        id = self.generate_id()
        self.graph_config['id'] = id
        self.graph_config['name'] = _graph_name
        self.graph_config["unit"] = _graph_unit
        self.graph_config["type"] = _graph_type
        self.graph_config["color"] = self.COLORS[_graph_color]
        msg, _request_success = self.__do_request()
        print(msg)
        return _request_success, id

    def __do_request(self):
        """ Do a API post, to create the graph. Return a tuple containing: \n
            msg - A string containing the success msg or an error msg specifying what caused the request to fail.\n
            is_success - A boolean for verification, if False you may want to try creating the user again.
        """
        response = requests.post(url=self.graph_endpoint, json=self.graph_config, headers=self.headers)
        log = response.json()
        msg, is_success = log.values()
        return msg, is_success

    def create_graph_url(self) -> str:
        """create the graph url, based on the user parameters"""
        return f"{self.graph_endpoint}/{self.graph_config['id']}.html"

    # makes parameters to be required to use its keywords
    def update_atributes(self, *, token=None, user_endpoint=None):
        """ Updates the graph atributes - token, graph_endpoint.\n
            You can pass the arguments as keywords
        """
        try:
            if token is not None:
                self.headers["X-USER-TOKEN"] = token
            if user_endpoint is not None:
                self.graph_endpoint = f"{user_endpoint}/graphs"
            else:
                print("No parameter specified, update suspended.")
        except TypeError as err:
            print("No parameter specified, update suspended.")





# graph = Graph("VdV1qI5V3V7-Cg$|", "https://pixe.la/v1/users/willianyamauti")
# graph.create_graph("teste3", "days", "int", "blue")
# url = graph.create_graph_url()
# print(url)
