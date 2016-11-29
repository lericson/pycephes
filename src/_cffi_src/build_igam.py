# Inspired by pyca/cryptography (Apache/BSD)

from cffi import FFI


ffi = FFI()
ffi.cdef("""
double igam(double s, double x);
double igamc(double s, double x);
""")
ffi.set_source(
    "_igam",
    """
double igam(double s, double x);
double igamc(double s, double x);
""",
    libraries=["md"],
)


if __name__ == '__main__':
    ffi.compile()
