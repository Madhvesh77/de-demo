from workshop.registry import ModuleRegistry
from workshop.menu import Menu
from workshop.config import config
from workshop.stages import Stage


def main():

    registry = ModuleRegistry()

    menu = Menu()

    while True:

        stage = Stage(config.stage)

        print()

        print("=" * 60)

        print("DATA ENGINEERING WORKSHOP")

        print("=" * 60)

        print()

        print(f"Current Stage : {stage}")

        modules = registry.enabled_modules(stage)

        menu.display(modules)

        choice = input("\nChoice : ").lower()

        if choice == "x":

            break

        if choice == "0":

            if config.stage < len(Stage):

                config.stage += 1

            continue

        if choice == "9":

            if config.stage > 1:

                config.stage -= 1

            continue

        try:

            choice = int(choice)

            modules[choice - 1].run()

        except Exception as ex:

            print(ex)

        input("\nPress ENTER...")


if __name__ == "__main__":

    main()