"""
CLIArgs Generic Command Line Interface (CLI) Toolset Library - Command Line Arguments Controller
"""

### Import Library/Modules ###

## Built-In Libraries
import sys
import os
import argparse

## Dependencies
import lib.toolset.toolset as toolset

class Initialize():
	"""
	Program Initialization

	1. Initialize argparse
	"""
	def __init__(self, parser=None, parser_opts=None, arguments=None, arg_list=None, namespace=None):
		"""
		:: Params
			parser : The parser you want to use (can be None)
				Type: argparse.ArgumentParser() object
				Optional: True
				Default: None

            		parser_opts : Options to pass to the generating parser
                		Type: Dictionary (Kwargs)
                		Optional: True
                		Default: None
                		Values:
                		    Key : Parameter Name
                		    Value : Parameter value
	
			arguments : All Arguments and their definitions here
				Type: List
				Values:
					[
						# Argument 1
						{
                					"flags" : ["flag-or-string"],
							"optionals" : {
								# ...
							}
						},
						# Argument 2
						{
                           		 		"flags" : ["flag-or-string"],
							"optionals" : {
								# ...
							}
						},
						...
					]
				Optional: True
				Default: None

			arg_list : A List of strings to parse for parse_args()
				Type: List
                		Optional: True
                		Default: None

            		namespace : A Namespace object to hold the variables
                		Type: Namespace
                		Optional: True
                		Default: None
		"""

		# Initialize Command Line Interface (CLI) Argument Controller class
		self.cliargs = toolset.Toolset.CLIArgsControl(parser, parser_opts)
		self.parser = self.cliargs.parser

		# Add Arguments
		number_of_arguments = len(arguments)
		for i in range(number_of_arguments):
			curr_arg = arguments[i]
			
            		# Retrieve Argument Details
            		# List
            		curr_arg_name_or_flags = curr_arg["flags"]

            		if "optionals" in curr_arg:
                		# Dictionary
                		curr_arg_optionals = curr_arg["optionals"]
            		else:
               		 	curr_arg_optionals = {}

			# Add current argument to Argument Parser
			self.cliargs.arg_add(curr_arg_name_or_flags, self.parser, **curr_arg_optionals)

		# Parse Arguments
		self.args = self.cliargs.arg_parse(self.parser, arg_list, namespace)

	def get_parser(self):
		return self.parser

	def get_args(self):
		return self.args
