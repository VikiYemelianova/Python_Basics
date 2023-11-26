user_input = int(input("Введіть числов від 0 до 8640000: "))

days = user_input // 86400
hours = (user_input % 86400) // 3600
min = (user_input % 3600) // 60
sec = user_input % 60

format_days = ('днів', 'дні', 'день')

format_hours = f'{hours:02}' if hours != 0 else '00'
format_min = f'{min:02}' if min != 0 else '00'
format_sec = f'{sec:02}' if sec != 0 else '00'

if days == 0:
    days_word = format_days[0]
elif days % 100 in range(11, 15):
    days_word = format_days[0]
else:
    last_num = days % 10
    if last_num == 1:
        days_word = format_days[2]
    elif 2 <= last_num <= 4 and 22 >= last_num <= 24:
        days_word = format_days[1]
    else:
        days_word = format_days[0]

print(f'{days} {days_word}, {format_hours}:{format_min}:{format_sec}')