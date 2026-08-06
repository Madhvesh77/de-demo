from workshop.core.module import WorkshopModule
from workshop.stages import Stage

from warehouse.init import initialize


class WarehouseModule(WorkshopModule):

    @property
    def name(self):
        return "Warehouse"

    @property
    def stage(self):
        return Stage.WAREHOUSE

    def run(self):
        initialize()