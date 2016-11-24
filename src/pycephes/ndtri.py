import numpy as np
from numba import njit, cffi_support

import _ndtri
from _ndtri import lib, ffi

cffi_support.register_module(_ndtri)

_ndtri = lib.ndtri


@njit
def ndtri(q):
    return _ndtri(q)
