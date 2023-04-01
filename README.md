# pa2-sample
Sample code for PA2 assignment

## How to Run (high-level)
* Clone the repository
* Install the dependencies
* Run the server
* Run the frontend
* Click "Make API Call" button to see the frontend upload based on backend

## Step by Step Commands
Here is the first few steps to clone the repo and run the backend

    git clone https://github.com/nigelbabu/pa2-sample.git
    cd pa2-sample
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    flask --app backend run --port 8001

Open a new terminal to run the frontend

    cd pa2-sample
    python3 -m venv/bin/activate
    python3 frontend.py
