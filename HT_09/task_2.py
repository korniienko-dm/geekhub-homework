"""
Task_2:
Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість
символів. Файл також додайте в репозиторій. На екран повинен вивестись
список із трьома блоками - символи з початку, із середини та з кінця файлу.
Кількість символів в блоках - та, яка введена в другому параметрі.
Придумайте самі, як обробляти помилку, наприклад, коли кількість символів
більша, ніж є в файлі або, наприклад, файл із двох символів і треба вивести
по одному символу, то що виводити на місці середнього блоку символів?).
Не забудьте додати перевірку чи файл існує.
"""


TEXT_FILE_PATH = "task_2_file/task_2_text.txt"


def file_exist_status(file_path: str) -> bool:
    """
    Check the existence of a file at the specified path.
    """
    try:
        with open(file_path, 'r'):
            return True
    except FileNotFoundError:
        print(f'FileNotFoundError: File "{file_path}" don\'t exist!')
        return False


def get_file_content(file_path: str) -> str:
    """
    Read and return the content of the file at the specified path.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read().replace('\n', '')
        return file_content


def get_content_validation_error(content: str, symbol_count: int) -> bool:
    """
    Validate if there is enough content to output three blocks, each with the specified symbol count.
    """
    if len(content) < symbol_count * 3:
        try:
            raise ValueError("ValueError: Number of characters in the file is less than required to output three blocks.")
        except ValueError as text_error:
            print(text_error)
            return False
    else:
        return True


def get_blocks_for_values(file_content: str, symbol_count: int, is_even: bool) -> list:
    """
    Return a list of text blocks with specified symbol count from the file content.
    If is_even is True, the function considers even values; otherwise, it considers odd values.
    """
    text_block_list = list()
    first_block_start = symbol_count
    last_block_start = symbol_count * -1

    if is_even:
        middle_block_start = len(file_content) // 2 - (symbol_count // 2)
        middle_block_end = len(file_content) // 2 + (symbol_count // 2)
    else:
        middle_block_start = (len(file_content) - symbol_count) // 2
        middle_block_end = (len(file_content) + symbol_count) // 2

    text_block_list.append(file_content[:first_block_start])
    text_block_list.append(file_content[middle_block_start:middle_block_end])
    text_block_list.append(file_content[last_block_start:])

    return text_block_list


def file_generate(file_path: str, symbol_count: int):
    "Generate a list of text blocks with the specified symbol count from the file content."

    file_content = get_file_content(file_path)

    if file_exist_status(file_path) is False:
        return "Stop work."

    if get_content_validation_error(file_content, symbol_count) is False:
        return "Stop work."

    if symbol_count % 2 == 0 and len(file_content) % 2 == 0:
        text_block_list = get_blocks_for_values(file_content, symbol_count, is_even=True)

    elif symbol_count % 2 != 0 and len(file_content) % 2 != 0:
        text_block_list = get_blocks_for_values(file_content, symbol_count, is_even=False)

    else:
        try:
            text_block_list = f'Error: Cannot build 3 blocks with number of characters:"{symbol_count}" and content length: "{len(file_content)}"'
            raise ValueError(text_block_list)
        except ValueError as text_error:
            return text_error

    return text_block_list


print(file_generate(file_path=TEXT_FILE_PATH, symbol_count=4))
