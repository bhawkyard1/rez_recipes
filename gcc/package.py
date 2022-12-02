name = "gcc"

version = "9.4.0"

description = (
    "The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as "
    "libraries for these languages (libstdc++,...). GCC was originally written as the compiler for the GNU operating "
    "system. The GNU system was developed to be 100% free software, free in the sense that it respects the user's "
    "freedom."
)

tools = ["gcc"]


@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "os-**"]
    return [expand_requires(*requires)]


def pre_build_commands():
    env.DOWNLOAD = (
        f"wget https://ftp.gnu.org/gnu/gcc/gcc-{this.version}/"
        f"gcc-{this.version}.tar.gz"
    )
    env.UNTAR = f"tar xzvf gcc-{this.version}.tar.gz"
    env.PREREQS = f"cd gcc-{this.version} && ./contrib/download_prerequisites"

    path = build.build_path
    if build.install:
        path = build.install_path

    env.CONFIGURE = (
        f"./gcc-{this.version}/configure --prefix={path} "
        f"--enable-languages=c,c++"
    )
    env.MAKE = "make -j 4"
    env.INSTALL = "make install -j 4"


build_command = """
echo $DOWNLOAD
$DOWNLOAD
echo $UNTAR
$UNTAR
echo $PREREQS
$PREREQS
echo $CONFIGURE
$CONFIGURE
echo $MAKE
$MAKE
echo $INSTALL
$INSTALL
"""


def commands():
    pass
