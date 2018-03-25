#! python3
# Password locker program - not secure!!

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print("Usage: python pw.py [account]")
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard")
else:
    print("No account named " + account)
