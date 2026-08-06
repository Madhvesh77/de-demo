from workshop.config import config
from workshop.menu import Menu
from workshop.stages import Stage


def main():

    current_stage = Stage(config.current_stage)

    while True:

        print("\n" + "=" * 60)
        print("DATA ENGINEERING WORKSHOP")
        print("=" * 60)

        print(f"\nCurrent Stage : {current_stage}\n")

        menu = Menu(current_stage)

        menu.display()

        try:

            choice = int(input("\nChoice : "))

        except ValueError:

            continue

        if choice == 0:

            break

        module = menu.get_module(choice)

        if module is None:

            print("\nInvalid Choice")

            continue

        print()

        print("=" * 60)

        print(f"Running {module.name}")

        print("=" * 60)

        module.run()

        input("\nPress ENTER to return to menu...")


if __name__ == "__main__":

    main()