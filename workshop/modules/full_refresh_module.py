from workshop.core.module import WorkshopModule
from workshop.stages import Stage

from etl.full_refresh import main


class FullRefreshModule(WorkshopModule):

    @property
    def name(self):
        return "Full Refresh ETL"

    @property
    def stage(self):
        return Stage.FULL_REFRESH

    def run(self):
        main()