import dotenv


def load_dotenv():
    # Get the path to the .env file
    dotenv_path = dotenv.find_dotenv()
    # Load the .env file
    dotenv.load_dotenv(dotenv_path)
