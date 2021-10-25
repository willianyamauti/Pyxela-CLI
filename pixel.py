import requests
import datetime as dt

# username = "willianyamauti"
endpoint = "https://pixe.la/v1/users/willianyamauti/graphs/e4v3sm54pe"
tok = "VdV1qI5V3V7-Cg$|"


class Pixel:
    """ The Pixel class is used for the management of pixels in the graph\n
        The class requires a Token and a endpoint to make modifications
    """

    # parameters to be used in the request
    pixel_config = {
        "date": "",
        "quantity": "",
    }

    # personal token to authorize access
    headers = {
        "X-USER-TOKEN": '',
    }

    def __init__(self, token: str, graph_endpoint: str):
        self.PIXEL_ENDPOINT = graph_endpoint
        self.headers["X-USER-TOKEN"] = token

    def manage_pixel(self, day: str, quantity: str, mode: str) -> bool:
        """ Manages a pixel in the graph, the options are: create, update and delete.\n
            If the pixel do not exists update will create the pixel instead
        """
        self.pixel_config["date"] = day
        self.pixel_config["quantity"] = quantity
        msg, is_success = self.__do_request(mode)
        print("Request Status: " + msg)
        return is_success

    def __do_request(self, mode: str) -> (str, bool):
        """Execute the request according to the given mode.\n
           create - will create a pixel,\n
           update - will update a pixel if it exist or create a new one in the given day\n
           delete - will delete a pixel\n
           the module return a tuple containing a str with the status of the request\n
           and a bool for the success of the request
        """
        modes = {
            "create": requests.post,
            "update": requests.put,
            "delete": requests.delete,
        }

        if mode in modes:
            # set the proper url for the request
            my_url = ""
            if mode != "create":
                my_url = f"{self.PIXEL_ENDPOINT}/{self.pixel_config['date']}"
            else:
                my_url = self.PIXEL_ENDPOINT
            func = modes[mode]
            response = func(url=my_url, json=self.pixel_config, headers=self.headers)
            log = response.json()
            msg, is_success = log.values()
            return msg, is_success
        else:
            print("Error, we don't have that option!")


# pixel = Pixel(tok, endpoint)
# print("Creating pixel - 20210915, 500")
# pixel.manage_pixel("20210915", "500", "create")
# print("Creating pixel using update pixel - 20210916, 1000")
# pixel.manage_pixel("20210916", "1000", "update")
# print("Updating pixel - 20210915, 1000")
# pixel.manage_pixel("20210915", "1000", "update")
# print("Creating pixel - 20210917, 500")
# pixel.manage_pixel("20210917", "500", "create")
# print("Deleting pixel - 20210917, 500")
# pixel.manage_pixel("20210915", "500", "delete")

