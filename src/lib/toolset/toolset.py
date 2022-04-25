"""
Library to the brains of the Generic Command Line Interface utility
"""

### Import Libraries/Modules ###

## Built-In
import sys
import os
import argparse

## Dependencies

class Toolset():
	"""
	Generic CLI Toolset class
	"""
	class CLIArgsControl():
		"""
		CLI Argument Management wrapper of argparse
		"""
		def __init__(self, parser=None):
			# Constructor
			if parser == None:
				self.parser = self.generate_parser()
			else:
				self.parser = parser

		def generate_parser(self):
			"""
			Initialize parser object
			"""
			parser = argparse.ArgumentParser()
			return parser

		def arg_add(self, short_opt, long_opt, parser=None, **arg_defn):
			"""
			:: Params
				short_opt : Short Option name (i.e. -o, -h)
					Type: String
				long_opt : Long Option name (i.e. --out, --help)
					Type: String
				arg_defn : Argument Definitions
					Type: kwargs (Variable Length Dictionary argument)
			"""
			if parser == None:
				# Default to using the constructor parser
				parser = self.parser
			parser.add_arguments(short_opt, long_opt, **arg_defn)
			return parser

		def arg_parse(self, parser):
			"""
			Parse the arguments parser
			"""
			args = parser.parse_args()
			return args
