while True:
    print('[1] Bratcko')
    print('[2] andra saker')
    print('[3] Avbryt')
    choice = int(input('Choice: '))
    if choice == 3:
        confirm = input('Vill du avsluta Y/N ')
        if confirm.lower() == 'y':
            break
    elif choice == 1:
        confirm = input('Jul sak 1 Y/N ')
        if confirm.lower() == 'y':
            print('julklapp')
            break
    elif choice == 2:
        confirm = input('Jul sak 2 Y/N ')
        if confirm.lower() == 'y':
            print('tomten')
            break