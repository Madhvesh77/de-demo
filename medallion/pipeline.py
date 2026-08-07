from medallion.silver import build as build_silver
from medallion.gold import build as build_gold


def build():

    print("Building Silver...")
    build_silver()

    print("Building Gold...")
    build_gold()

    print("Medallion Refresh Complete")


if __name__ == "__main__":
    build()