from spack import *
from llnl.util import filesystem as fs


class ExampleDependency(Package):
    url      = "http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz"
    version('1.0.6', '00b516f4704d4a7cb50a1d97e6e8e15b')

    depends_on('python')

    def install(self, spec, prefix):
        fs.touch(fs.join_path(prefix, 'INSTALL_DONE'))
