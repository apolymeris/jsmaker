#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Usage: make.py [ -h|--help ] [ -d|--debug ] [ -r|--release ]
"""

import getopt, sys, os
from config import CONFIG


class Module:
	"""
	Basic Module
	"""
	def __init__( self, obj ):
		self.output = obj["output"]
		self.dirs = obj["dirs"]
		self.run()
	
	def run( self ):
		raise NotImplemented


class CSS_Module( Module ):
	"""
	CSS Module
	"""
	def __init__( self ):
		raise NotImplemented


class JS_Module( Module ):
	"""
	JavaScript Module
	"""
	def __init__( self, obj ):
		self.output = obj["output"]
		self.dirs = obj["dirs"]
		self.run() 
		
	def run( self ):
		""" start builder """
		output = open( self.output, "w" )
		output.write( self.get_content() )
		output.close()
		print self.output + " created successfully."

	def get_content( self ):
		""" return module content """
		content = ""
		for dir in self.dirs:
			content += self.get_dir_content( dir )
		return content
		
	def get_dir_content( self, dir ):
		""" return dir content """
		files = os.listdir( dir )
		content = ""
		for file in files:
			if os.path.isdir( dir + "/" + file ): # recursion
				content += self.get_dir_content( dir + "/" + file )
			else:
				f = open( dir + "/" + file, "r" )
				content += "\n" + f.read() + "\n"
				f.close()
		return content 

def compress( obj ):
    for module in CONFIG[ "MODULES" ]:
		JS_Module( module )

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