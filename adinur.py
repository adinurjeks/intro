def check(password):
    digits = 0
    letters = 0

    for symbol in password:
        if symbol.isdigit():
            digits += 1
        elif symbol.isalpha():
            letters += 1
    
    return digits >= 2 and letters >= 7

def show_menu():
    print("   🔐 ПРОВЕРКА СЛОЖНОСТИ ПАРОЛЯ")
    print("1 — Проверить пароль")
    print("0 — Выход")
