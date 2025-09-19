import os
import sys

def rename_files(directory, prefix):
	try:
		for idx, filename in enumerate(os.listdir(directory)):
			ext = os.path.splitext(filename)[1]
			new_name = f'{prefix}_{idx}{ext}'
			os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
		print('files renamed successfully.')
	except Exception as e:
		print(f'Error: {e}')


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('Usage: python filename.py')

	else:
		rename_files(sys.argv[1], sys.argv[2])