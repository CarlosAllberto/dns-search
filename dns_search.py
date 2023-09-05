import socket
import argparse

def show_banner():
	print('''
 ____  _   _ ____                      _     
|  _ \| \ | / ___|  ___  __ _ _ __ ___| |__  
| | | |  \| \___ \ / _ \/ _` | '__/ __| '_ \\ 
| |_| | |\\  |___) |  __/ (_| | | | (__| | | |
|____/|_| \_|____/ \\___|\__,_|_|  \___|_| |_|

	--[ Coded by : King D a.k.a N3utr0n
	--[ Team : FHC (FR13NDs Hackers Club)
	''')

def get_ip(host):
	try:
		ip = socket.gethostbyname(host)
		return ip
	except:
		return 'A'

def get_name(host):
	try:
		name = socket.gethostbyaddr(host)[0]
		return name
	except:
		return 'A'

def readFile(filename):
	try:
		filename = open(filename, 'r').read().split('\n')
		return filename
	except Exception as error:
		print('[-] Erro ao tentar abrir o arquivo.')
		return False

def make(subdomain, domain):
	return subdomain + '.' + domain

def DNSearchIP(domain, file):
	filename = readFile(file)
	print('[+] Target :', domain)
	print('[!] Subdomain file :', file)
	print('[*] Searching Subdomains and IP\'s...\n')
	for subdomain in filename:
		host = make(subdomain, domain)
		ip = get_ip(host)
		if ip != 'A':
			print('[+] Domain :', host, ' | IP :', ip)

	print('\n[!] Feito...')

show_banner()
parser = argparse.ArgumentParser(description='This tool search for subdomains in websites')
parser.add_argument('-d', '--domain', help='The Domain target', required=True)
parser.add_argument('-f', '--filename', help='Filename contains subdomains')
parser.add_argument('-i', '--ip', help='Return IP', action='store_true')
parser.add_argument('-n', '--name', help='Return Name', action='store_true')

args = parser.parse_args()

if args.ip:
	if args.filename == None:
		args.filename = 'dns.txt'
	DNSearchIP(args.domain, args.filename)

elif args.name:
	name = get_name(args.domain)
	print('[+] IP :', args.domain, ' | Domain :', name)
else:
	print(args.help)
