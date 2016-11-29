# Inspired by pyca/cryptography (Apache/BSD)

from cffi import FFI


ffi = FFI()
ffi.cdef("""
double chdtr( double df, double x );
double chdtri( double df, double y );
double chdtrc( double df, double x );
""")
ffi.set_source(
    "_chi2",
    """
double chdtr( double df, double x );
double chdtri( double df, double y );
double chdtrc( double df, double x );
""",
    libraries=["md"],
)


if __name__ == '__main__':
    ffi.compile()
