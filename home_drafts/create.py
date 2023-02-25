import sys
import re

id = sys.argv[1]
name = sys.argv[2]


def main(id, name):
    # Відкриваємо файл зі старим кодом та змінними
    with open('python_lessons/home_drafts/crated.py', 'r') as f:
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


    with open('python_lessons/home_drafts/crated_hbn1.py', 'w') as f_out:
        f_out.write(result)

main(id, name)
