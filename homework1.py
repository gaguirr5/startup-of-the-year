try:
    while True:
        menu = """
            MENU
            a – Add travel log
            d – Remove travel log
            u – Update travel log
            o – Output entire log in console
            s – Save travel log to database
            q – Quit """
        userinput = input('Enter option: ')
        if userinput.lower() == 'a':
            print('You pressed a')
        if userinput.lower() == 'q':
            print('you quit with q')
            break

except ValueError:
    print('Input must be from Menu')
