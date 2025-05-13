#!/bin/bash

# Lancer le bot DesMana pour Scales
cd /home/leo/bots-disord/bot-disc-scales
source .venv/bin/activate
nohup python3 main.py &

# Sortir du venv
deactivate
