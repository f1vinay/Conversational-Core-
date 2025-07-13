@echo off
echo Setting up virtual environment...
python -m venv venv
call venv\Scripts\activate

echo Installing requirements...
pip install -r requirements.txt

echo Starting Chat Assistant...
python chat.py
