from pathlib import Path

def remove_all_files(directory_path: str):
    dir_path = Path(directory_path)
    remaining_data = list(dir_path.iterdir())
    print(f"Total number of files/folders remaining in {dir_path} are {len(remaining_data)}")

    for file in dir_path.iterdir():
        file_string = str(file)
        temp = file_string.split('/')[-1]
        if temp[0] == '.':
            print(f"{file} is hidden!")
            continue

        Path(file).unlink()
        print(file)
        print(f"{file} has been deleted from {dir_path} folder.")
    
    remaining_data = list(dir_path.iterdir())
    print(f"Total number of files/folders remaining in {dir_path} are {len(remaining_data)}")

remove_all_files("/Users/apoorvsingh/Downloads")