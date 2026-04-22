def check(password):
    digits = 0
    letters = 0

    for symbol in password:
        if symbol.isdigit():
            digits += 1
        elif symbol.isalpha():
            letters += 1
    
    return digits >= 2 and letters >= 7

def show():
    print("   🔐 ПРОВЕРКА СЛОЖНОСТИ ПАРОЛЯ")
    print("1 — Проверить пароль")
    print("0 — Выход")

while True:
    show()
    choice = input("Выберите действие: ")
    if choice == "1":
        password = input("\nВведите пароль: ")
        if check(password):
            print("\n✅ Пароль подходит!")
        else:
            print("\n❌ Ошибка:")
            print("   • минимум 2 цифры")
            print("   • минимум 7 букв")
    elif choice == "0":
        print("\n👋 Программа завершена")
        break
    else:
        print("\n⚠ Неверный выбор, попробуйте снова")