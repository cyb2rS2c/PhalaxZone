#!/bin/bash
git clone https://github.com/cyb2rS2c/PhalaxZone.git
cd PhalaxZone/phalaxzone
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi
source myenv/bin/activate
pip install -r requirements.txt
chmod +x phx.sh;sudo python3 phalaxzone.py
