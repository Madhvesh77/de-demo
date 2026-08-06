from workshop.registry import ModuleRegistry


class Menu:

    def __init__(self, stage):

        self.registry = ModuleRegistry()

        self.modules = self.registry.get_by_stage(stage)

    def display(self):

        print("\nAvailable Actions\n")

        for index, module in enumerate(self.modules, start=1):

            print(f"{index}. {module.name}")

        print("\n0. Exit")

    def get_module(self, choice):

        if choice < 1 or choice > len(self.modules):

            return None

        return self.modules[choice - 1]