import numpy as np
from numba import njit, cffi_support

import _igam
from _igam import lib, ffi

cffi_support.register_module(_igam)

lower = lib.igam
upper = lib.igamc
