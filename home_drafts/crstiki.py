desk_null = '''
| |
-+-+-
| |
-+-+-
| |'''

desk_player = """
7 | 8 | 9
--+-+--
4 | 5 | 6
--+-+--
1 | 2 | 3
"""
desk_lists = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
d = desk_lists
playing = True
while playing:

    print("Введи цифру где хочешь поставить 0")
    user_input = int(input())
    for i in desk_lists:
        if i == user_input:
            desk_lists[user_input] = '0'
    desk_lists[user_input] = '0'
    desk_game = f"""
    {d[7]} | {d[8]} | {d[9]}
    --+-+--
    {d[4]} | {d[5]} | {d[6]}
    --+-+--
    {d[1]} | {d[2]} | {d[3]}
    """
    print(desk_game)
    if d[7] and d[8] and d[9] == '0' or d[4] and d[5] and d[6] == '0' or d[1] and d[2] and d[3] == '0' or d[7] and d[4] and d[1] == '0' or d[8] and d[5] and d[2] == '0' or d[9] and d[6] and d[3] == '0':
        print("Ты выиграл")
        break