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
        def __init__(self, parser=None, parser_opts=None):
            """
            Constructor

            :: Params
                parser : Personal parser to use without generating a new one 
                    Type: argparse.ArgumentParser()
                    Optional: True
                    Default: None

                parser_opts : Options to pass when generating the parser
                    Type: Dictionary
                    Optional: True
                    Default: None
                    Values:
                        Key : Parameters
                        Value : Argument
            """
            if parser == None:
                if parser_opts == None:
                    self.parser = self.generate_parser()
                else:
                    self.parser = self.generate_parser(**parser_opts)
            else:
                self.parser = parser

        def generate_parser(self, **parser_kwargs):
            """
            Initialize parser object
            """
            if parser_kwargs == None:
                parser = argparse.ArgumentParser()
            else:
                parser = argparse.ArgumentParser(**parser_kwargs)
            return parser

        def arg_add(self, name_or_flags=None, parser=None, **arg_defn):
            """
            :: Params
                #short_opt : Short Option name (i.e. -o, -h)
                #    Type: String
                # long_opt : Long Option name (i.e. --out, --help)
                #    Type: String
                name_or_flags : A Name/List of option strings (i.e. foo, -f, --foo)
                    Type: String/List
                parser : Your parser object
                    Type: argparse.ArgumentParser()
                    Default: self.parser
                arg_defn : Argument Definitions
                    Type: kwargs (Variable Length Dictionary argument)
            """
            if parser == None:
                # Default to using the constructor parser
                parser = self.parser
            parser.add_argument(name_or_flags, **arg_defn)
            return parser

        def arg_parse(self, parser, arg_list=None, namespace=None):
            """
            Parse the arguments parser

            :: Params
                parser: Your parser Object
                    Type: argparse.ArgumentParser()
                arg_list: List of strings to parse
                    Optional: Yes
                    Default: taken from sys.argv
                namespace: Namespace/object to take attributes (i.e. Namespace(variable="Value"))
                    Type: namespace object
                    Default: a new empty Namespace object
            """
            if arg_list == None and namespace == None:
                args = parser.parse_args()
            elif arg_list == None:
                args = parser.parse_args(namespace)
            elif namespace == None:
                args = parser.parse_args(arg_list)
            else:
                args = parser.parse_args(arg_list, namespace)
            return args
