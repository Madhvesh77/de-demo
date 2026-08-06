from pathlib import Path

import yaml


def load_catalog():

    return yaml.safe_load(

        Path(

            "semantic/catalog.yaml"

        ).read_text()

    )