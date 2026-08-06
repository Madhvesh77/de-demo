class Menu:

    def display(self, modules):

        print()

        for index, module in enumerate(modules, start=1):

            print(f"{index}. {module.name}")

        print()

        print("9. Previous Stage")

        print("0. Next Stage")

        print("x. Exit")