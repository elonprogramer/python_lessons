import sys
import re
import random

id = sys.argv[1]
# name = sys.argv[2]
# name_list = list(name)
# new_name = ""
#
# new_name = random.choice(name_list)


def main(id, name):
    # Відкриваємо файл зі старим кодом та змінними
    with open('text_in', 'r') as f:
        file_contents = f.read()
    # Replace the variables
    print(f"{file_contents=}")
    old_pattern = "(TG_CHANNEL_ID = -\d+)"
    match = re.search(old_pattern, file_contents)
    old_replace_var = match.group(1)
    # print(match)
    print(f'{old_replace_var=}')

    new_replace_var = 'TG_CHANNEL_ID = -3333333'
    print(f'{new_replace_var=}')

    result = re.sub(old_replace_var, new_replace_var, file_contents)
    print(f'{file_contents=}')
    print(f'{result=}')


    with open('text_out', 'w') as f_out:
        f_out.write(result)


    # new_value = f"TG_CHANNEL_ID = {id}"
    #
    #
    # file_contents = file_contents.replace(old_pattern, new_value)

    # Create a new file with the updated data and old code
    # new_filename = f'tg_id_{name}.py'
    # with open(new_filename, 'w') as f:
    #     f.write(file_contents)

name = 'ddddd'

main(id, name)