#!/bin/sh
set -ex
python3 -c "import requests; print(requests.get('http://localhost:8080/api/status').status_code)" | grep 200
