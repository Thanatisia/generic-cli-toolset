"""
A simple but powerful Command Line Interface utility powered by argparse that will print the result to standard output (stdout), allowing scripting capabilities

- Usable in programs like dmenu or rofi

:: Background

Powered by argparse, his toolset targets to be a generic CLI toolset as a foundation/base, allowing users to take and create their own functions that returns a variable. 
User just needs to modify the parser to include their personal cli arguments and they have made their own scriptable, portable, modular CLI program.

This project was inspired by my shellscripting adventures as well as seeing rofi/dmenu scripting capabilities.

I also aim to be able to use this toolset to create a simple lemonbar scripting environment for use in my workflow

:: Features
	+ Modifiable - this is a generic CLI toolset aiming to give users the convenience of making their own scriptable CLI 
	+ portable - Just keep the base toolchain/toolset as a repository or backup and you can reuse it however much you like
	+ scriptable - this is my main focus as I do use programs such as rofi and dmenu that allows for advance scripting capabilities as well as automation

:: Contacts
Author(s) : 
	- Asura (https://github.com/Thanatisia)

:: Dependencies
	+ python
	+ pip
	+ argparse

:: Program Design
	-h | --help : Displays this help message
	-v | --version : Prints the program's version and other program info
	-o | --get-opts : Returns all options in list format

:: Program Information
Program Name : generic-cli-toolset
Version History:
	- 2022-04-25 1434H : v0.1.0
		- Initial creation
"""

### Import Libraries/Modules ###

## Built-in Libaries
import sys
import os
import argparse

## Dependencies ##
import lib.toolset.toolset as toolset
import lib.toolset.cliargs as cliargs

options = {
	"help" : ["-h", "--help"],
	"version" : ["-v", "--version"],
}

def print_help():
    """
	Print the Help menu
	"""
    print("Help:")
    for label, opt_list in options.items():
        print("\t{} : {}".format(label, opt_list))

def print_version():
    """
    Print the version info
    """
    print("Version: {}, {} Made by {}".format("v0.1.0", "CLIArgs : Generic CLI Toolset (Name is horrible, sorry, still a WIP)", "Asura (Thanatisia)"))

def init():
    """
    Initialization
    """
    global genericli_toolset, genericli, cliargs_obj, args

    # Initialize classes
    genericli_toolset = toolset.Toolset()
    genericli = genericli_toolset.CLIArgsControl()

    # Initialize CLI Argument Controller
    cliargs_obj = cliargs.Initialize(None, 
        {
            "add_help" : False
        }, [
        {
            "short_opt" : "-h",
            "long_opt" : "--help",
            "optionals" : {

            }
        },
        {
            "short_opt" : "-v",
            "long_opt" : "--version",
            "optionals" : {

            }
        },	
        {
            "short_opt" : "-o",
            "long_opt" : "--get-opts",
            "optionals" : {

            }
        },
    ])

    # Get arguments
    args = cliargs_obj.get_args()

    # Output

def setup():
    """
    Basic Setup
    """
    init()

def main():
    """ 
    Process Arguments
    """
    if args.help:
        # Display Help message
        print_help()

    if args.version:
        # Display Version
        print_version()

    if args.get_opts:
        # Output
        opt_str = ' '.join(options)
        print(opt_str)

if __name__ == "__main__":
    setup()
    main()
