# subfinder_automated
This script automates and extends the functionality of subfinder in a way that not only to find subdomains, but also permutate TLDs.

# Install
install needed python libraries:
```shell
pip3 install subprocess
pip3 install argparse
```
then install [subfinder](https://github.com/projectdiscovery/subfinder) and you are ready to go

# Usage
```shell
python subfinder_automated.py -d google -w seclists/Discovery/DNS/tlds.txt
```

