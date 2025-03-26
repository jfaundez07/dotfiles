#!/usr/bin/env python3

import sys
import json
import subprocess

def get_player_status(player=None):
    try:
        player_option = ['-p', player] if player else []
        
        status = subprocess.check_output(['playerctl'] + player_option + ['status'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
        artist = subprocess.check_output(['playerctl'] + player_option + ['metadata', 'artist'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
        title = subprocess.check_output(['playerctl'] + player_option + ['metadata', 'title'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
        art_url = subprocess.check_output(['playerctl'] + player_option + ['metadata', 'mpris:artUrl'], stderr=subprocess.DEVNULL).decode('utf-8').strip()

        icon = "🎵"
        if player == "spotify":
            icon = ""
        elif player == "firefox":
            icon = ""
        
        output = {
            "icon": icon,
            "text": f"{artist} - {title} ({status})",
            "art_url": art_url
        }
        print(json.dumps(output))

    except subprocess.CalledProcessError:
        output = {
            "icon": "🎵",
            "text": "Player not running",
            "art_url": ""
        }
        print(json.dumps(output))

if __name__ == "__main__":
    player = sys.argv[1] if len(sys.argv) > 1 else None
    get_player_status(player)