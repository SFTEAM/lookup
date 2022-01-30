import requests
import os
import json
import sys
import colorama
import time
from colorama import Fore
from time import sleep

os.system("cls & title lookup made by mkay")

host = input(f"[{Fore.YELLOW}INPUT{Fore.RESET}] IP: ")

os.system("cls & title lookup made by mkay")

r = requests.get(f'https://json.geoiplookup.io/{host}')

g = requests.get(f'https://vpn.geoiplookup.io/{host}')

geo = r.json()
isp = geo['isp']
country = geo['country_name']
city = geo['city']
ccode = geo['country_code']
cur = geo['currency_code']
asn = geo['asn']
lati = geo['latitude']
long = geo['longitude']
geo = g.json()
vpn = geo['badip']

print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] IP: {host}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] ISP: {isp}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] CITY: {city}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] COUNTRY: {country}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] COUNTRY CODE: {ccode}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] CURRENCY: {cur}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] ASN: {asn}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] LATITUDE: {lati}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] LONGITUDE: {long}")
print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] VPN: {vpn}")
time.sleep(300)