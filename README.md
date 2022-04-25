# Generic CLI Toolset (In Python)

A simple but powerful Command Line Interface utility powered by argparse that will print the result to standard output (stdout), allowing scripting capabilities

- Usable in programs like dmenu or rofi

## Table of Contents
- [Information](#information)
- [Setup](#setup)
- [Documentation](#documentation)
- [Contacts](#contacts)

## Information

### Background

Powered by argparse, his toolset targets to be a generic CLI toolset as a foundation/base, allowing users to take and create their own functions that returns a variable. 
User just needs to modify the parser to include their personal cli arguments and they have made their own scriptable, portable, modular CLI program.

This project was inspired by my shellscripting adventures as well as seeing rofi/dmenu scripting capabilities.

I also aim to be able to use this toolset to create a simple lemonbar scripting environment for use in my workflow

### Features

+ Modifiable - this is a generic CLI toolset aiming to give users the convenience of making their own scriptable CLI 
+ portable - Just keep the base toolchain/toolset as a repository or backup and you can reuse it however much you like
+ scriptable - this is my main focus as I do use programs such as rofi and dmenu that allows for advance scripting capabilities as well as automation

### Program Information

+ Project Name : generic-cli-toolset

## Setup

### Pre-Requisites

### Dependencies
+ python
+ pip
+ argparse

### Installation/Compiling

## Documentation

### Using on its own

#### Synopsis/Syntax

python main.py [{options} [arguments]]

#### Parameters/Arguments

+ -h | --help : Displays this help message
+ -v | --version : Displays program version and other relevant information
+ -o | --get-opts : Returns all options in list format (stdout will be seperated by spaces)

#### Usage

+ Get options
	```console
	$> python main.py --get-opts
	$> list of options
	```

### Using as a Library

#### Import Library

- Import 'toolset'
	```python
	import toolset.toolset 
	```
- Import 'cliargs'
	```python
	import toolset.cliargs
	```

#### Functions

- toolset
	- Toolset
		- CLIArgControl
			+ generate_parser
			+ arg_add
			+ arg_parse

- cliargs
	- Initialize
		- get_parser()
		- get_args() 

### Customization/Configuration

- cliargs.Initialize
	```python
	arg_definitions = [
		## Arguments here

		# Argument 1
		{
			"short_opt" : "",
			"long_opt" : "",
			"optionals" : {
				# Your Optionals Here
			}
		},
		# Argument n
		{
			"short_opt" : "",
			"long_opt" : "",
			"optionals" : {
				# Your Optionals Here
			}
		}
	]
	```

## Contacts

- Author(s) : 
	- [Asura/Thanatisia](https://github.com/Thanatisia)