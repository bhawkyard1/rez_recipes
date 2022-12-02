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
    env.PULL_COMMAND = "git clone git://gcc.gnu.org/git/gcc.git"
    env.CD_REPO = "cd gcc"
    env.CHECKOUT_COMMAND = f"git checkout releases/gcc-{this.version}"
    path = build.build_path
    if build.install:
        path = build.install_path
    env.CONFIGURE_COMMAND = (
        f"gcc-{this.version}/configure --prefix={path} "
        f"--enable-languages=c,c++"
    )


build_command = """
echo $PULL_COMMAND
$PULL_COMMAND
echo $CD_REPO
$CD_REPO
echo $CHECKOUT_COMMAND
$CHECKOUT_COMMAND
"""


def commands():
    pass
