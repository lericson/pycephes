import numpy as np
from numba import cffi_support, float32, float64, vectorize

import _igam
from _igam import lib, ffi

cffi_support.register_module(_igam)
_igam = lib.igam
_igamc = lib.igamc

@vectorize([float64(float64, float64),
            float32(float32, float32)])
def lower(s, x):
    return _igam(s, x)

@vectorize([float64(float64, float64),
            float32(float32, float32)])
def upper(s, x):
    return _igamc(s, x)
