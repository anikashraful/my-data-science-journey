import sys


def count_words(filename):
	try:
		with open(filename, 'r') as file:
			text = file.read()
			words = text.split()
			print(f'{filename} has {len(words)} words.')
	except FileNotFoundError:
		print(f'Error: File not found: {filename}')
	except Exception as e:
		print(f'An error occurred: {str(e)}')

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage: python wordcounter.py')
	else:
		count_words(sys.argv[1])