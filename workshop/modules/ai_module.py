from workshop.core.module import WorkshopModule
from workshop.stages import Stage

from ai.analyst import main


class AIModule(WorkshopModule):

    @property
    def name(self):
        return "AI Analyst"

    @property
    def stage(self):
        return Stage.SEMANTIC_LAYER

    def run(self):
        main()