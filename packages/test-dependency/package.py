from spack import *


class TestDependency(Package):
    homepage = "http://www.example.com"
    url      = "http://www.example.com/a-1.0.tar.gz"

    version('1.0', 'hash1.0')
    version('1.1', 'hash1.1')
    version('2.0', 'hash2.0')

    depends_on('boost           +system +filesystem', when='@:1.1.999')
    depends_on('boost@:1.65.999 +system +filesystem', when='@1.2:')

    def install(self, spec, prefix):
        touch(join_path(prefix, 'an_installation_file'))
