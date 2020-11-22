# -*- coding: utf-8 -*-
# flake8: noqa


# -------------- Add path of _k2.so into sys.path --------------
import os as _os
import sys as _sys

_current_module = _sys.modules[__name__]
_k2_dir = _os.path.dirname(_current_module.__file__)

if not hasattr(_current_module, "__path__"):
    __path__ = [_k2_dir]
elif _k2_dir not in __path__:
    __path__.append(_k2_dir)
_sys.path.append(__path__)


# ---------------------- Absolute import  ----------------------
from k2._k2 import IntArray2Size
from k2._k2 import FbWeightType

from k2.python import k2

# ---------------------- Setting __all__  ----------------------

# Add more symbols in this file's scope that with names not start with '_'.
__all__.extend(
    [_s for _s in dir() if not _s.startswith("_") and _s not in __all__]
)

# Explicitly avoid importing the wild star, like "from k2 import *".
# This give a suggestion for users to follow the conventional usage --
# just import needed symbols:
#   from k2 import Fsa
#   from k2.fsa import Fsa
__all__.extend(["DO_NOT_WILD_IMPORT"])
