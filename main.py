from imaplib import IMAP4_SSL
import email
import getpass

# IMAP PROTOCOL SPECIFICATION: https://tools.ietf.org/html/rfc3501
# imaplib documentation: https://docs.python.org/3.8/library/imaplib.html

# delete an email:
# imap_client.store('email_id', '+FLAGS', '\\DELETED')


host = input('Enter imap host: ')

imap_client = IMAP4_SSL(host)

imap_client.noop()

user = input("Enter imap user: ")
pw = getpass.getpass(prompt='Enter imap password:')
imap_client.login(user, pw)

imap_client.list()

from pprint import pprint

pprint(imap_client.list())

imap_client.select(mailbox="Spam", readonly=False)

imap_client.search(None, 'all')

imap_client.search(None, '1')
