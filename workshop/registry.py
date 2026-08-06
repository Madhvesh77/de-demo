from workshop.modules.generator_module import GeneratorModule
from workshop.modules.warehouse_module import WarehouseModule
from workshop.modules.full_refresh_module import FullRefreshModule
from workshop.modules.incremental_module import IncrementalModule
from workshop.modules.ai_module import AIModule


class ModuleRegistry:

    def __init__(self):

        self.modules = [
            GeneratorModule(),
            WarehouseModule(),
            FullRefreshModule(),
            IncrementalModule(),
            AIModule(),
        ]

    def get_all(self):
        return self.modules

    def get_by_stage(self, stage):

        return [
            module
            for module in self.modules
            if module.stage <= stage
        ]