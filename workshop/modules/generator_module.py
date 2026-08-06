from workshop.core.module import WorkshopModule
from workshop.stages import Stage

from generator.run import main as generator_main


class GeneratorModule(WorkshopModule):

    @property
    def name(self):
        return "Data Generator"

    @property
    def stage(self):
        return Stage.OLTP

    def run(self):
        generator_main()