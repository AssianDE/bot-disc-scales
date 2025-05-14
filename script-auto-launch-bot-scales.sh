#!/bin/bash

# Lancer le bot DesMana pour Scales
cd /home/leo/bots-disord/bot-disc-scales
source .venv/bin/activate
nohup python3 main.py > nohuplog 2>&1 &
echo $! > /home/leo/bots-disord/bot-disc-scales/bot-scales.pid

# Sortir du venv
deactivate
