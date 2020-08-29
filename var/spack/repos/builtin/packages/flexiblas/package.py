# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Flexiblas(CMakePackage):
    """A BLAS and LAPACK wrapper library with runtime exchangable backends
    """

    homepage = "https://www.mpi-magdeburg.mpg.de/projects/flexiblas"
    url      = "https://csc.mpi-magdeburg.mpg.de/mpcsc/software/flexiblas/flexiblas-3.0.3.tar.gz"

    version('3.0.3', sha256='926ab31cf56f0618aec34da85314f3b48b6deb661b4e9d6e6a99dc37872b5341')

    # virtual dependency
    provides('blas')
    provides('lapack')

    @property
    def blas_cmake_args(self):
        return [
            CMakePackage.define('BLA_STATIC', False),
            CMakePackage.define('BLA_VENDOR', 'FlexiBLAS'),
        ]

    @property
    def lapack_cmake_args(self):
        return self.blas_cmake_args
