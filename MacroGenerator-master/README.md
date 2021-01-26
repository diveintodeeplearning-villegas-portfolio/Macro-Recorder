# What is __MacroGenerator__

MacroGenerator is a python script - for people who want to create a bot for automate testing or build a little macro scripts.

## Prerequisit

1. (Macro Recorder](https://www.jitbit.com/macro-recorder/)
2. Python 2.6.4 or newer is recommended

# Using MacroGenerator

## Import Script

```python
from MacroGenerator import MacroGenerator
```

## Functions

```python

# The constructor
# name = file name that you want to created
def __init__(self, target_name):


# Write a content in a file line by line
def write_file(self, command):


# Insert ctrl + v (paste) in our macro file
def paste_clipboard(self):


# Set clipboard with argument text string
def set_clipboard(self, text):


# Wait for x millisecconds, e.g. 1000 = 1 seccond
def set_delay(self, delay):


# Type text with keyboard
# {#crlf#} which means a new line (but doesnt mean it press 'Enter' key)
def typetext(self, text):

  
# Click a mouse in current position	
# mouse_event: ['Click', 'RightClick']
def mouse_click(self, mouse_event = 'Click'):


# YOU MUST CLOSE A FILE AFTER YOU'VE OPENED IT UP
# close a file that we've opened
def close(self):
  self.__fopen.close();
```

## Building Script

### Python

```bash
python [file_name.py]
```

### [Tips] Sublime Text

On Sublime Text you can open *.py file and press 'Ctrl + B' for building a script.


## Usage example

- [helloMacro](https://github.com/blackSourcez/MacroGenerator/blob/master/sample/helloMacro.py)








