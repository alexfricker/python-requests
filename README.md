# Python and Requests for API usage
Quick little repo on using `requests` with python to consume APIs. This example will use Purecloud to retrieve an access token and use the token for data retrieval (POST and GET requests). The process should be similar for whatever types of requests you need to make (probably still just POST or GET).

## Setup/Installation
Clone the repo to your machine and open a terminal inside of the directory. Run the following to create a virtual environment and install required packages:
- `python -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

## Executing script
Execute the script by running the following command in your terminal (you still need to be in the project folder):
- `python main.py`

You will be prompted to enter an access token - message me and I will give it to you.