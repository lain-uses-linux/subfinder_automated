

import argparse
import subprocess

def get_arguments():
    parser = argparse.ArgumentParser(description="bruteforces subdomains")
    parser.add_argument("-w", "--w", dest="wordlist", help="path to tlds wordlist")
    parser.add_argument("-d", "--domain", dest="domain", help="domain name to scan without tld")
    args = parser.parse_args()
    return args

user_arguments = get_arguments()

if not user_arguments.wordlist or not user_arguments.domain:
    print('[!] check arguments, use --help')
    exit()

domain = user_arguments.domain
wordlist = user_arguments.wordlist

with open(wordlist, 'r') as wordlist_file:
    wordlist_file = wordlist_file.read().split('\n')

    for tld in wordlist_file:
        if tld[0] == '.':
            tld = tld[1:]
        filename = 'subdomains_'+domain+'.'+tld
        subprocess.run(["subfinder", "-d", domain+'.'+tld, "-o", filename], capture_output=True, text=True)
        print('[+] scanned for ' + domain + '.' + tld + '; saved in ' + filename)



