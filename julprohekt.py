while True:
    print('[1] Berätelse om tomten')
    print('[2] Berätelse om Harmanen')
    print('[3] Avbryt')
    choice = int(input('Choice: '))
    if choice == 3:
        confirm = input('Vill du avsluta Y/N ')
        if confirm.lower() == 'y':
            break
    elif choice == 1:
        confirm = input('Tomten gillar mycket kakor med mjölk Y/N ')
        if confirm.lower() == 'y':
            print('tomten äter minst 24 kakor per dygn')
            break
    elif choice == 2:
        confirm = input('Harmanen gillar inte kakor med mjölk Y/N ')
        if confirm.lower() == 'y':
            print('Harmanen kan inte äta 1 kaka då spyr han')
            break