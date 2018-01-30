from spack import *


class ExampleDependent(Package):
    homepage = "http://www.example.com"
    url      = "http://www.example.com/example-1.2.3.tar.gz"

    version('1.2.3', '0123456789abcdef0123456789abcdef')

    depends_on('python')

    def install(self, spec, prefix):
        make()
        make('install')

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        pass
