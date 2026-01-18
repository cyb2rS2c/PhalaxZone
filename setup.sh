#!/bin/bash
cd phalaxzone
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi
source myenv/bin/activate
pip install -r requirements.txt
chmod +x phx.sh;sudo python3 phalaxzone.py
