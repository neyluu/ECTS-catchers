import os
import re

import src.config.Settings as Settings

SETTINGS_FILE_NAME = "config/settings.settings"

def loadSettings():
    print("Loading settings...")

    if not os.path.isfile(SETTINGS_FILE_NAME):
        print("ERROR: file with settings not found! Loaded base settings")
        return

    with open(SETTINGS_FILE_NAME, "r") as file:
        lines = file.readlines()
        if len(lines) < 4:
            print("ERROR: file is corrupted! Loaded base settings")
            return

        targetFPS = int(_loadLine(lines[0], r'targetFPS:\s(\d+)'))
        if targetFPS == -1:
            print("ERROR: failed to load target FPS! Loaded base setting")
        elif targetFPS not in (30, 60, 144):
            print("ERROR: wrong value of target FPS! Loaded base setting")
        else:
            Settings.TARGET_FPS = targetFPS

        soundMaster = float(_loadLine(lines[1], r'soundMaster:\s*([0-9]*\.?[0-9]+)'))
        if soundMaster == -1:
            print("ERROR: failed to load sound master! Loaded base setting")
        elif not _musicInBound(soundMaster):
            print("ERROR: wrong value of sound master! Loaded base setting")
        else:
            Settings.sounds.setMaster(soundMaster)

        soundMusic = float(_loadLine(lines[2], r'soundMusic:\s*([0-9]*\.?[0-9]+)'))
        if soundMusic == -1:
            print("ERROR: failed to load sound music! Loaded base setting")
        elif not _musicInBound(soundMusic):
            print("ERROR: wrong value of sound music! Loaded base setting")
        else:
            Settings.sounds.setMusic(soundMusic)

        soundSFX = float(_loadLine(lines[3], r'soundSFX:\s*([0-9]*\.?[0-9]+)'))
        if soundSFX == -1:
            print("ERROR: failed to load sound SFX! Loaded base setting")
        elif not _musicInBound(soundSFX):
            print("ERROR: wrong value of sound sfx! Loaded base setting")
        else:
            Settings.sounds.setSFX(soundSFX)

        fpsCounter = _loadLine(lines[4], r'fpsCounter:\s*(True|False)')
        if fpsCounter == -1:
            print("ERROR: failed to load fps counter! Loaded base setting")
        else:
            Settings.FPS_COUNTER = False if fpsCounter == "False" else True


    print("Settings loaded!")


def saveSettings():
    os.makedirs("config", exist_ok=True)

    with open(SETTINGS_FILE_NAME, "w+") as file:
        file.write(f"targetFPS: {Settings.TARGET_FPS}\n")
        file.write(f"soundMaster: {Settings.sounds.master}\n")
        file.write(f"soundMusic: {Settings.sounds.musicBase}\n")
        file.write(f"soundSFX: {Settings.sounds.sfxBase}\n")
        file.write(f"fpsCounter: {Settings.FPS_COUNTER}\n")

    print("Settings saved!")


def _loadLine(line, regex):
    match = re.search(regex, line)
    if match:
        return match.group(1)
    else:
        return -1


def _musicInBound(musicVolume : float):
    return 0.0 <= musicVolume <= 1.0