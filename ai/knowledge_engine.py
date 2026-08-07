from pathlib import Path
import yaml


def load_yaml(path):
    return yaml.safe_load(Path(path).read_text())


def get_metric(metric_name):

    metric = metric_name.lower()

    path = Path("semantic/metrics")

    for file in path.glob("*.yaml"):

        data = load_yaml(file)

        if data["name"].lower() == metric:

            return data

    return None


def get_entity(entity):

    path = Path(
        f"semantic/entities/{entity}.yaml"
    )

    if path.exists():

        return load_yaml(path)

    return None