def check_password(password):
    digits = 0
    letters = 0

    for symbol in password:
        if symbol.isdigit():
            digits += 1
        elif symbol.isalpha():
            letters += 1

    return digits >= 2 and letters >= 7


def show_menu():
    print("\n" + "=" * 40)
    print("   🔐 ПРОВЕРКА СЛОЖНОСТИ ПАРОЛЯ")
    print("=" * 40)
    print("1 — Проверить пароль")
    print("0 — Выход")
    print("=" * 40)


# основной цикл программы
while True:
    show_menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        password = input("\nВведите пароль: ")

        if check_password(password):
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