import os


class Utils:
    def clearScreen(self):
        if os.name == 'posix':  # for mac and linux uses 'posix'
            _ = os.system('clear')
        else:
            _ = os.system('cls')  # for windows platfrom