from generator.scenarios.seed import seed_database


def print_menu():
    print("=" * 35)
    print("   ShopSmart Data Generator")
    print("=" * 35)
    print("1. Seed Initial Database")
    print("2. Exit")
    print("=" * 35)


def main():

    while True:

        print_menu()

        choice = input("Choice: ").strip()

        if choice == "1":
            seed_database()

        elif choice == "2":
            print("\nGoodbye 👋")
            break

        else:
            print("\nInvalid option.\n")


if __name__ == "__main__":
    main()