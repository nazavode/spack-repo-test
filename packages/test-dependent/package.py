from spack import *


class TestDependent(Package):
    homepage = "http://www.example.com"
    url      = "http://www.example.com/a-1.0.tar.gz"

    version('1.0', 'hash1.0')

    depends_on('boost')
    depends_on('test-dependency')

    def install(self, spec, prefix):
        touch(join_path(prefix, 'an_installation_file'))
