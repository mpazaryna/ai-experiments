# Dotenv

## Walk directory for .env

In this monorepo, I've put the .env file in the root, so it only needs to be managed in one location.

```py
import dotenv

# Get the path to the .env file
dotenv_path = dotenv.find_dotenv()

# Load the .env file
dotenv.load_dotenv(dotenv_path)

# Get the value of an environment variable
value = os.environ['MY_ENV_VAR']
```
