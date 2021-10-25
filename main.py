from backend import Backend

BACKEND = Backend()


def show_title():
    print("""
            ██████╗ ██╗   ██╗██╗  ██╗███████╗██╗      █████╗ 
            ██╔══██╗╚██╗ ██╔╝╚██╗██╔╝██╔════╝██║     ██╔══██╗
            ██████╔╝ ╚████╔╝  ╚███╔╝ █████╗  ██║     ███████║
            ██╔═══╝   ╚██╔╝   ██╔██╗ ██╔══╝  ██║     ██╔══██║
            ██║        ██║   ██╔╝ ██╗███████╗███████╗██║  ██║
            ╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                        Pixela's Pyhton CLI helper 
        """)

    print(f"Version : 0.01  Author: Satoshi\n"
          f"This is a free cli for creating and managing pixela graphs utilizing the free api.\n"
          f"For now, is possible perform the following tasks:\n\n"
          f"USER  | Create new user\n"
          f"      | Access existing user\n"
          f"GRAPH | Create a new graph\n"
          f"      | Access am existing graph\n"
          f"PIXEL | Manage pixel placement(create,update,delete)\n\n"
          f"All results are given in url form at the time, just copy to your browser to visualize the graphs."
          )

    print("Not all options are implemented at the moment, but the script is functional, more updates to include:\n"
          "* Web application\n"
          "* All API functionalities")

    print("Just Follow the on screen instruction to properly set or manage a graph.\n")
    print("-" * 100)


def show_parent_menu():
    print(f"\nEnter the desired option\n"
          f"[1] Access a existing user\n"
          f"[2] Create a new User\n")


def do_log_in():
    print(f"Enter your Pixela credentials\n")
    BACKEND.access_existing_user()

def do_create_new_user():


def show_child_menu_1():
    print(f"\nEnter the desired option\n"
          f"[1] Access a existing user\n"
          f"[2] Create a new User\n")


show_title()
show_parent_menu()

# TODO implement the heuristic
# TODO implement a data base for the created pixela graphs, accounts, and questions related the graph
# TODO refazer backend.py para nao ter inputs
