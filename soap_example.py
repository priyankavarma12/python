#Python Program for Soap requests

import webbrowser,sys

webbrowser.open('https://python.org')


address = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/' + address)
