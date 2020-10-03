# /bin/bash

cd /spark/app
rm -Rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
/spark/bin/spark-submit --master spark://spark-master:7077 main.py