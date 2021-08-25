from Tools.json2csv import json2csv
from Tools.csv2json import csv2json
from Tools.colors import colors as c
import sys
def convert_csv(input, output):
	print(f"{c.cyan}[TOOL] converting {input} to {output}, please wait...{c.w}")
	csv2json(input, output)
def convert_json(input, output):
	print(f"{c.cyan}[TOOL] converting {input} to {output}, please wait...{c.w}")
	json2csv(input, output)
if __name__ == '__main__':
	args = sys.argv
	try:
		convert_type = args[1]
		input = args[2]
		output = args[3]
	except:
		pass
	if len(args) != 4:
		print(f"{c.red}[TOOL] Invalid usage!\nExample: python main.py csv2json input.csv output.json{c.w}")
	elif convert_type == "csv2json":
		print(len(args))
		convert_csv(input, output)
	elif convert_type == "json2csv":
		convert_json(input, output)
	elif convert_type != "csv2json" and convert_type != "json2csv":
		print(f"{c.red}[TOOL] Please choose a valid converting type (json2csv or csv2json){c.w}")
