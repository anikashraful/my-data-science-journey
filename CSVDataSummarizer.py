import os
import sys

def summarize_csv(filename):
	try:
		with open(filename, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			row = list(reader)
			print(f'Rows: {len(rows)}')
			if rows:
				print('Column:', row[0].keys())
	except FileNotFoundError:
		print('file not found')
	except Exception as e:
		print(f'Error: {e}')

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage: python csvsummarizer.py')
	else:
		summarize_csv(sys.argv[1])