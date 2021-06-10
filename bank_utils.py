def make_menu(options):
    print("Wybierz numerek i nacisnij ENTER")
    a = 1
    for x in options:
        print(str(a) + ". " + str(x))
        a += 1
    print(str(a) + ". Wyjscie")
    return int(input())
