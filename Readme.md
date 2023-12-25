# Installation for Debian

```sh
sudo apt-get install gcc git git-lfs python3-venv jq -y
git clone https://github.com/patnaikshekhar/llama_service
cd llama_service
git clone git@hf.co:meta-llama/Llama-2-7b-chat-hf
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# Run the service

```sh
uvicorn main:app --reload
```

# Get a prediction

```sh
curl -X POST -d @./sample.json -H 'Content-Type: application/json'  http://localhost:8000/api/v1/chat
```