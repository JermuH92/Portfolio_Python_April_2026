import os

def count_files(path):
	try:
		files = os.listdir(path)
	except FileNotFoundError:
		print(f"Skipping broken path: {path}")
		return 0
	
	except PermissionError:
		print(f"No read permission for directory: {path}")

	count = 0

	for item in files:
		full_path = os.path.join(path, item)
		
		try:
			if os.path.isfile(full_path):
				count += 1
			elif os.path.isdir(full_path):
				count += count_files(full_path)
		except FileNotFoundError:
			print(f"Skipped a shadow file: {full_path}")
			continue
		
	return count

if __name__ == "__main__":
	test_path = ".."

	total = count_files(test_path)
	print(f"From directory {test_path} and it's sub-directories found a total of {total} files")

			