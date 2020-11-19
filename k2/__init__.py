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

from k2.python.k2 import array
from k2.python.k2 import aux_labels
from k2.python.k2 import fsa
from k2.python.k2 import fsa_algo
from k2.python.k2 import fsa_equivalent
from k2.python.k2 import fsa_util
from k2.python.k2 import properties
from k2.python.k2 import weights

from k2.python.k2.array import (
    DoubleArray1,
    FloatArray1,
    IntArray1,
    IntArray2,
    LogSumArcDerivs,
    StridedIntArray1,
)
from k2.python.k2.aux_labels import (
    AuxLabels,
    AuxLabels1Mapper,
    AuxLabels2Mapper,
    FstInverter,
)
from k2.python.k2.fsa import (
    Arc,
    Fsa,
)
from k2.python.k2.fsa_algo import (
    ArcSorter,
    Connection,
    DeterminizerLogSum,
    DeterminizerMax,
    EpsilonsRemoverLogSum,
    EpsilonsRemoverMax,
    Intersection,
    TopSorter,
    arc_sort,
)
from k2.python.k2.fsa_equivalent import (
    RandPath,
    is_rand_equivalent,
    is_rand_equivalent_after_rmeps_pruned_logsum,
    is_rand_equivalent_logsum_weight,
    is_rand_equivalent_max_weight,
)
from k2.python.k2.fsa_util import (
    str_to_fsa,
)
from k2.python.k2.properties import (
    has_self_loops,
    is_acyclic,
    is_arc_sorted,
    is_connected,
    is_deterministic,
    is_empty,
    is_epsilon_free,
    is_top_sorted,
    is_valid,
)
from k2.python.k2.weights import (
    WfsaWithFbWeights,
)

# -------------------- Setting __all__  --------------------

# Use __all__ to show the suggested API for users.
__all__ = [
    "Arc",
    "ArcSorter",
    "AuxLabels",
    "AuxLabels1Mapper",
    "AuxLabels2Mapper",
    "Connection",
    "DeterminizerLogSum",
    "DeterminizerMax",
    "DoubleArray1",
    "EpsilonsRemoverLogSum",
    "EpsilonsRemoverMax",
    "FloatArray1",
    "Fsa",
    "FstInverter",
    "IntArray1",
    "IntArray2",
    "Intersection",
    "LogSumArcDerivs",
    "RandPath",
    "StridedIntArray1",
    "TopSorter",
    "WfsaWithFbWeights",
    "arc_sort",
    "array",
    "aux_labels",
    "fsa",
    "fsa_algo",
    "fsa_equivalent",
    "fsa_util",
    "has_self_loops",
    "is_acyclic",
    "is_arc_sorted",
    "is_connected",
    "is_deterministic",
    "is_empty",
    "is_epsilon_free",
    "is_rand_equivalent",
    "is_rand_equivalent_after_rmeps_pruned_logsum",
    "is_rand_equivalent_logsum_weight",
    "is_rand_equivalent_max_weight",
    "is_top_sorted",
    "is_valid",
    "properties",
    "str_to_fsa",
    "weights",
]


# Add more symbols in this file's scope that with names not start with '_'.
__all__.extend(
    [_s for _s in dir() if not _s.startswith("_") and _s not in __all__]
)

# Just keep these var names start with '_'
__version__ = "0.1.0"
_names_with_underscore = [
    "__version__",
]
__all__.extend([_s for _s in _names_with_underscore])

# To explicitly avoid importing the wild star, like "from k2 import *"
# The suggested conventional usage for user, just import needed symbols:
#   from k2 import Fsa
#   from k2.fsa import Fsa
__all__.extend(["DO_NOT_WILD_IMPORT"])
