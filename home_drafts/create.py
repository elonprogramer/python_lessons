import sys
import random

id = sys.argv[1]
name = sys.argv[2]
name_list = list(name)
new_name = ""

new_name = random.choice(name_list)


def main(id, name):
    # Відкриваємо файл зі старим кодом та змінними
    with open('kinopomichnik/sites/uaserial.py', 'r') as f:
        file_contents = f.read()
    # Replace the variables
    old__value = "TG_CHANNEL_ID"
    new__value = f"TG_CHANNEL_ID = {id}"
    file_contents = file_contents.replace(old__value, new__value)

    # Create a new file with the updated data and old code
    new_filename = f'kinopomichnik/sites/tg_id_{name}.py'
    with open(new_filename, 'w') as f:
        f.write(file_contents)


main(id, name)