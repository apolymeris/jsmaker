#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Usage: make.py [ -h|--help ] [ -d|--debug ] [ -r|--release ]
"""

import getopt, sys
from config import CONFIG

def compress( obj ):
    print CONFIG
    print obj

def main():
    try:
        opts, args = getopt.getopt( sys.argv[1:], "hrd", [ "help", "release", "debug" ] )
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    
    cfg = {
        "release"       : False,
        "debug"         : False,
        "modules"    : []
    }   
    for o, a in opts:
        if o in ( "-r", "--release" ):
            cfg[ "release" ] = True
        if o in ( "-d", "--debug" ):
            cfg[ "debug" ] = True
        if o in ( "-h", "--help" ):
            print __doc__
            sys.exit(0)
    compress( cfg )
if __name__ == "__main__":
	main()