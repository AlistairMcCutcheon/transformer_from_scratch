import importlib.util
import sys
from pathlib import Path
from types import ModuleType

class ConfigReader:

    @staticmethod
    def read_config(path: str) -> ModuleType:
        # Reads a path to a python module and returns the module as an object
        # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
        module_name = Path(path).stem
        spec = importlib.util.spec_from_file_location(Path(path).stem, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module