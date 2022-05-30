import config

def print_debug(message: str):
    if config.debug_printing:
        print(message)