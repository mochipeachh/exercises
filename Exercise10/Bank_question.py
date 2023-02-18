import getpass

correct_pin = 1043
success = "congrats your pin is correct"
failure = "wrong pin please try again"
maxattempts = 3

for attempt in range(maxattempts):
    supplied_pin = int(getpass.getpass(prompt="enter your pin"))
    if correct_pin == supplied_pin:
        print(success)
    else:
        print(failure)
        print(f'attempts tried = {attempt + 1}')

