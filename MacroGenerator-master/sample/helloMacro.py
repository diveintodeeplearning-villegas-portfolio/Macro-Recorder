import re
import sys
sys.path.insert(0, '../')
from MacroGenerator import MacroGenerator

file_name = "helloMacro.mcr";

def generate():

	# create a file
	mcr_file = MacroGenerator(file_name);

	# wait for 1 seccond
	mcr_file.set_delay(1000);
	
	# press Window + R key
	mcr_file.sendkey('LWindows','KeyDown');
	mcr_file.sendkey('R','KeyDown');
	mcr_file.sendkey('R','KeyUp');
	mcr_file.sendkey('LWindows','KeyUp');

	# wait for 1 seccond
	mcr_file.set_delay(1000);
	mcr_file.typetext('notepad');
	mcr_file.sendkey('Enter','KeyDown');
	mcr_file.set_delay(1000);

	# type notepad and new line
	mcr_file.typetext('notepad\n\n\n\nThis is from MacroGenerator');
	mcr_file.set_delay(2000);

	# press Alt + F4 key
	mcr_file.sendkey('AltLeft','KeyDown');
	mcr_file.sendkey('F4','KeyDown');
	mcr_file.sendkey('F4','KeyUp');
	mcr_file.sendkey('AltLeft','KeyUp');
	mcr_file.set_delay(2000);
	mcr_file.sendkey('N','KeyPress');

	# [!IMPORTANT] you must close a file after finish generating script
	mcr_file.close();

def main():
	generate();

main();
