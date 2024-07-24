# Test task for junior python rpa position
import os

path = 'C:\\Users\\alibe\\PycharmProjects\\RPA_test_proj\\TestTask'


def categorize_files_by_type(folder_path: str) -> dict[str: list]:
    result_dict = {}
    if os.path.isfile(folder_path):
        file_name, extension = os.path.splitext(folder_path)
        result_dict[extension] = file_name
    else:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                _dir, extension = os.path.splitext(file_path)
                if extension not in result_dict:
                    result_dict[extension] = []
                result_dict[extension].append(file_path)
    return result_dict


result = categorize_files_by_type('C:\\Users\\alibe\\PycharmProjects\\RPA_test_proj\\TestTask\\README.txt')
print(result)