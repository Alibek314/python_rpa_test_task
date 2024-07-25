# Test task for junior python rpa position
import os


def categorize_files_by_type(folder_path: str, min_file_size=None) -> dict[str: list]:
    """The function searches for all the files in given root directory &
    returns dictionary with file extensions as keys and file locations as it's value"""
    if not os.path.exists(folder_path):  # here we check if root folder exists
        return f"The path '{folder_path}' does not exist."
    elif not os.path.isdir(folder_path):  # here we check if root folder is directory
        return f"The root path should point to the directory.\nGot '{folder_path}' instead."

    result_dict = {}

    # Using the os.walk() function to recursively check for files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Here we can filter files by size
            if min_file_size is not None:
                current_size = os.path.getsize(file_path)
                if current_size < min_file_size:
                    continue

            _dir, extension = os.path.splitext(file_path)
            if extension not in result_dict:
                result_dict[extension] = []
            result_dict[extension].append(file_path)

    # Here we can change output to required format, simply by uncommenting following block
    # (couldn't write accurate tests for this format at the moment)

    # output_format = "{" + "\n"
    # for key, value in result_dict.items():
    #     output_format += f"  '{key}': {value},\n"
    # output_format = output_format.rstrip(",\n") + "\n}"
    # return output_format

    return result_dict


result = categorize_files_by_type()
print(result)
