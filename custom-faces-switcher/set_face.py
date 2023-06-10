# -*- coding: utf-8 -*-

import re
import os
import sys
import subprocess


start_pattern = r"ui.faces.look_r = "
end_pattern_custom = r"ui.faces.png = false"
end_pattern_original = r"ui.faces.png = true"
config_file = "/etc/pwnagotchi/config.toml"
custom_snnipet = "/custom-faces-switcher/custom-faces.snip"
original_snnipet = "/custom-faces-switcher/original-faces.snip"
start_pwnagotchi = "systemctl start pwnagotchi"
stop_pwnagotchi = "systemctl stop pwnagotchi"

def process_argument(argument):
    case_value = argument.lower()
    print("Stop pwnagotchi service")
    execute_command(stop_pwnagotchi)

    if case_value == "custom":
        try:
            print("Setting custom")
            update_config_file(config_file, start_pattern, end_pattern_custom, custom_snnipet)

        except subprocess.CalledProcessError as e:
            print("Error:", e.output.decode())

    elif case_value == "original":
        try:
            print("Setting original")
            update_config_file(config_file, start_pattern, end_pattern_original, original_snnipet)

        except subprocess.CalledProcessError as e:
            print("Error:", e.output.decode())

    else:
        print("Invalid args")

    print("Restarting pwnagotchi")
    execute_command(start_pwnagotchi)


def update_config_file(config_file, start_pattern, end_pattern, replacement_snippet):
    try:
        #execute_command(stop_pwnagotchi)

        with open(config_file, "r") as file:
            configfile = file.read()

        with open(replacement_snippet, "r") as file:
            snnipet = file.read()

        pattern = re.compile(fr"{re.escape(start_pattern)}(.*?){re.escape(end_pattern)}", re.DOTALL)
        modified_code = re.sub(pattern, lambda x: snnipet, configfile, count=1)

        with open(config_file, "w") as file:
            file.write(modified_code)

        #execute_command(start_pwnagotchi)

    except Exception as e:
        print("Error:", e)


def execute_command(command):
    try:
        subprocess.call(command, shell=True)
    except Exception as e:
        print("Error:", e)


def show_help():
    print("Use: python set_face.py [option]")
    print("Available options:")
    print("  custom - Enable custom faces")
    print("  original - Disable custom faces")


if len(sys.argv) < 2 or sys.argv[1] == "--help":
    show_help()
    sys.exit()

argumento = sys.argv[1]

process_argument(argumento)
