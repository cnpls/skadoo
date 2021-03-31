rm -rf venv
python -m venv venv
venv/scripts/python.exe -m pip install --upgrade pip
venv/scripts/pip install -r requirements.txt -r requirements-dev.txt