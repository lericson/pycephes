import numpy as np
from numba import cffi_support, float32, float64, vectorize

import _chi2
from _chi2 import lib, ffi

cffi_support.register_module(_chi2)
_chdtr = lib.chdtr
_chdtrc = lib.chdtrc
_chdtri = lib.chdtri

@vectorize([float64(float64, float64),
            float32(float32, float32)])
def cdf(x, df):
    return _chdtr(df, x)

@vectorize([float64(float64, float64),
            float32(float32, float32)])
def ppf(p, df):
    return _chdtri(df, 1.0-p)

@vectorize([float64(float64, float64),
            float32(float32, float32)])
def sf(p, df):
    return _chdtrc(df, p)

@vectorize([float64(float64, float64),
            float32(float32, float32)])
def isf(p, df):
    return _chdtri(df, p)
