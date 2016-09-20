#!/usr/bin/env python
from distutils.core import setup
import re

__author__ = "Jason Sahl"
__credits__ = ["Jason Sahl"]
__license__ = "GPL v3"
__version__ = "1.0"
__maintainer__ = "Jason Sahl"
__email__ = "jsahl@tgen.org"
__status__ = "Development"
 
long_description = """WG-FAST, genotype
phylogenetically from a NASP formatted SNP
matrix
"""

setup(name='wg_fast',
      version=__version__,
      description='whole genome focused array SNP typing',
      author=__maintainer__,
      author_email=__email__,
      maintainer=__maintainer__,
      maintainer_email=__email__,
      packages=['wg_fast'],
      package_data = {'wg_fast': ['data/*.fasta']},
      long_description=long_description,
      scripts = ['wgfast.py', 'bin/AddOrReplaceReadGroups.jar', 'bin/bwa', 'bin/CreateSequenceDictionary.jar', 'bin/samtools', 'bin/trimmomatic-0.30.jar'],
      data_files=[('', ['wg_fast/data/illumina_adapters_all.fasta'])]
)
