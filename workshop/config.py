from dataclasses import dataclass


@dataclass
class WorkshopConfig:

    current_stage: int = 3


config = WorkshopConfig()