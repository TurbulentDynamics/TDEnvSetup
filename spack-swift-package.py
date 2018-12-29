# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Swift(Package):
    """Swift is a high-performance system programming language. It has a clean and modern syntax, offers seamless access to existing C and Objective-C code and frameworks, and is memory safe by default.  Although inspired by Objective-C and many other languages, Swift is not itself a C-derived language. As a complete and independent language, Swift packages core features like flow control, data structures, and functions, with high-level constructs like objects, protocols, closures, and generics. Swift embraces modules, eliminating the need for headers and the code duplication they entail.
"""

    homepage = "https://swift.org"
    url      = "https://swift.org/builds/swift-4.2.1-release/ubuntu1604/swift-4.2.1-RELEASE/swift-4.2.1-RELEASE-ubuntu16.04.tar.gz"
    version('4.2.1-RELEASE-ubuntu16.04', sha256='4a17bef7b02bb6480cd72282fd67463c12131bad013b79bc721c8cb2a5b83fd1')

    family = 'compiler'  # Used by lmod

    #depends_on('git')
    #depends_on('cmake@3.4.3:', type='build')
    depends_on('cmake')
    depends_on('ninja')
    depends_on('llvm' )
    #depends_on('python')
    depends_on('uuid')
    #depends_on('libicu-dev')
    #depends_on('icu-devtools')
    #depends_on('libbsd-dev')
    #depends_on('libedit-dev')
    depends_on('libxml2')
    #depends_on('sqlite3')
    depends_on('swig')
    #depends_on('libpython-dev')
    depends_on('ncurses')
    depends_on('pkg-config')
    #depends_on('libblocksruntime-dev')
    #depends_on('libcurl4-openssl-dev')
    #depends_on('systemtap-sdt-dev')
    #depends_on('tzdata')
    depends_on('rsync')



    def install(self, spec, prefix):
        make()
        make('install')
