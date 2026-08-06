from workshop.config import config
from workshop.stages import Stage
from workshop.registry import ModuleRegistry


def main():

    registry = ModuleRegistry()

    print("=" * 60)
    print("DATA ENGINEERING WORKSHOP")
    print("=" * 60)

    current_stage = Stage(config.current_stage)

    print(f"\nCurrent Stage : {current_stage}\n")

    print("Available Modules")
    print("-" * 60)

    for module in registry.get_by_stage(current_stage):

        print(f"✓ {module.name}")


if __name__ == "__main__":
    main()