import importlib
import inspect
import logging
import pkgutil
import sys

from app import db


def import_models():
    """Auto import all classes. Note that this will load all classes, not just model classes.
    It also does not support nested packages. """
    this_module = sys.modules[__name__]
    LOG = logging.getLogger(this_module.__name__)

    for loader, module_name, is_pkg in pkgutil.iter_modules(
            this_module.__path__, this_module.__name__ + '.'):
        module = importlib.import_module(module_name, loader.path)
        for name, _object in inspect.getmembers(module, inspect.isclass):
            if isinstance(_object, type(db.Model)):
                globals()[name] = _object
                LOG.debug("Imported model '%s.%s'", module_name, name)
                # print("%s.%s" % (module_name, name))
