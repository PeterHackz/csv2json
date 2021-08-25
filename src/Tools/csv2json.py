from csv2json import convert, load_csv, save_json
from Tools.colors import colors as c
def csv2json(path, output):
	with open(path) as r,open(output, 'w') as w:
		try:
			convert(r, w)
			print(f"{c.green}[TOOL] Succesfully converted {path} to {output}!{c.w}")
		except Exception as e:
			print(f"{c.red}[TOOL] An error has occured!\nERROR:\n{e}{c.w}")
