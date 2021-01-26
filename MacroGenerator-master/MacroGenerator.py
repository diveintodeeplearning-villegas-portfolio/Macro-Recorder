import re

"""

This script used for generating macro file (.mcr) for Macro Recorder
you can download at https://www.jitbit.com/macro-recorder/

"""

__author__ = "Ayuth Mangmesap (blackSource)"

class MacroGenerator:

	def __init__(self, target_name):
		self.target_name = target_name;
		self.__fopen = open(target_name,"w");

	def write_file(self, command):
		self.__fopen.write(command + '\n');

	def paste_clipboard(self):
		self.write_file('Keyboard : ControlLeft : KeyDown')
		self.write_file('Keyboard : V : KeyDown')
		self.write_file('Keyboard : V : KeyUp')
		self.write_file('Keyboard : ControlLeft : KeyUp')

	def set_clipboard(self, text):
		self.write_file('SET CLIPBOARD : {0} : 0 : Please enter the text to store in clipboard:'.format(text))

	def set_delay(self, delay):
		self.write_file('DELAY : {0}'.format(delay));

	#
	# keys e.g. ['Enter', 'ControlLeft', 'AltLeft', 'ShiftLeft', 'LWindows', 'NumPad1', 'F1', 'Tab']
	# key_event: ['KeyPress', 'KeyUp', 'KeyDown']
	#
	def sendkey(self, key, key_event = 'KeyPress'):
		self.write_file('Keyboard : {0} : {1}'.format(key,key_event));

	#
	# type text with keyboard
	# {#crlf#} = new line (but doesnt mean it press 'Enter' key)
	#
	def typetext(self, text):
		self.write_file('TYPE TEXT : {0}'.format(re.sub(r'\n', '{#crlf#}', text)))

	"""
	Click a mouse in current position	
	mouse_event: ['Click', 'RightClick']

	"""
	def mouse_click(self, mouse_event = 'Click'):
		self.write_file('Mouse : 0 : 0 : {0} : 0 : 1 : 0'.format(mouse_event));

	# close a file
	def close(self):
		self.__fopen.close();
