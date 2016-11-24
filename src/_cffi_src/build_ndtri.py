# Inspired by pyca/cryptography (Apache/BSD)

from cffi import FFI


ffi = FFI()
ffi.cdef("""
double ndtri(double y0);
""")
ffi.set_source(
    "_ndtri",
    """
double ndtri(double y0);
""",
    libraries=["md"],
)


if __name__ == '__main__':
    ffi.compile()
