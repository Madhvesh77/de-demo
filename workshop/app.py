from workshop.config import config

from workshop.stages import Stage


def main():

    print("=" * 60)

    print("DATA ENGINEERING WORKSHOP")

    print("=" * 60)

    print()

    print(f"Current Stage : {Stage(config.current_stage).name}")


if __name__ == "__main__":

    main()