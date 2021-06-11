from collections import namedtuple

VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel")
version_info = VersionInfo(major=1, minor=0, micro=0, releaselevel="alpha")

__version__ = "v{}.{}.{}-{}".format(
    version_info.major,
    version_info.minor,
    version_info.micro,
    version_info.releaselevel,
).replace("\n", "")
