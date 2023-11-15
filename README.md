# AI and Machine Learning Experiments

👇 Spin up a cloud development environment:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/mpazaryna/ai-experiments?quickstart=1)

## GitHub Codespaces

Codespaces is a cloud development environment that can be spun up in a few seconds. In this environment, there's an in-browser app preview that allows one to create and preview a Streamlit app on the cloud.

More info about [GitHub Codespaces](https://github.com/features/codespaces).

## Create Python environment

```sh
python3 -m venv venv
source venv/bin/activate
deactivate
```

### Install the required dependencies

``` bash
pip install -r requirements.txt
```

### Walk directory for .env

```py
import dotenv

# Get the path to the .env file
dotenv_path = dotenv.find_dotenv()

# Load the .env file
dotenv.load_dotenv(dotenv_path)

# Get the value of an environment variable
value = os.environ['MY_ENV_VAR']
```
