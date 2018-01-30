from spack import *
from spack.environment import EnvironmentModifications
from llnl.util import filesystem as fs


class ExampleDependent(Package):
    url      = "http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz"
    version('1.0.6', '00b516f4704d4a7cb50a1d97e6e8e15b')

    depends_on('example-dependency')

    def install(self, spec, prefix):
        to_be_sourced = fs.join_path(prefix, 'SOURCE_ME')
        with open(to_be_sourced, 'w') as f:
            f.write('export SOURCE_ME_HAS_BEEN_SOURCED=1')
        EnvironmentModifications.from_sourcing_file(to_be_sourced).apply_modifications()
        fs.touch(fs.join_path(prefix, 'INSTALL_DONE'))
