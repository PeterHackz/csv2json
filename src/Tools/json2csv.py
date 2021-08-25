import pandas as pd
from Tools.colors import colors as c
def json2csv(input, output):
	df = pd.read_json (input)
	try:
		export_csv = df.to_csv (output, index = None, header=True)
		print(f"{c.green}[TOOL] Succesfully converted {input} to {output}!{c.w}")
	except Exception as e:
		print(f"{c.red}[TOOL] An error has occured!\nERROR:\n{e}{c.w}")
