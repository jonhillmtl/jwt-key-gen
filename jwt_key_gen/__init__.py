from jwcrypto import jwk
from termcolor import colored
from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-v", action="store_true", dest="verbose", help="verbose output")
(options, args) = parser.parse_args()

def main():
    key = jwk.JWK(generate='oct', size=256)
    key.export()    

    try:
        if not options.verbose:
            print(key._key['k'])
        else:
            print("Generated key: {0}".format(key._key['k']))
            print(colored('Success', 'green'))
    except KeyError as e:
        if options.verbose:
            print(colored('Something went wrong generating the key.', 'red'))
    except AttributeError as e:
        if options.verbose:
            print(colored('Something went wrong generating the key.', 'red'))

