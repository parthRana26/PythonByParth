from datetime import datetime

current_hour = int(datetime.now().strftime('%H'))
if current_hour<12:
    print('Good morning')
elif 12<=current_hour<18:
    print('Good afternoon')
else:
    print('Good Evening')