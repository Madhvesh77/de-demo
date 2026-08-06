from workshop.core.module import WorkshopModule
from workshop.stages import Stage

from etl.incremental import main


class IncrementalModule(WorkshopModule):

    @property
    def name(self):
        return "Incremental ETL"

    @property
    def stage(self):
        return Stage.INCREMENTAL

    def run(self):
        main()