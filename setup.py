"""
Dependencies:
- pymatbridge: call MATLAB using Python
... buggy and limited features


"""



import os
import sys
# from pymatbridge import Matlab


# sys.path.append('/Users/stephane/Documents/git/takumi/fapm/cine_local')
# matlab_path = '/Applications/MATLAB_R2019a.app/bin/matlab'


# faqm_dir = os.path.split(os.path.realpath(__file__))[0]
# matlabdir = os.path.join(faqm_dir, 'matlab_codes')


# DATA ARCHITECTURE
# scriptdir, scriptname = os.path.split(os.path.realpath(__file__))

# mlab = Matlab(executable=matlab_path)
# mlabstart = mlab.start()
# mlab.run_code('addpath %s; savepath;' % matlabdir)

# print('DONE')
# print('... MATLAB may crash by this process, but the setup was successful.')
# mlab.quit()

from setuptools import setup, find_packages

setup(
    name='tflow',
    version='0.0.1',
    url='https://github.com/tmatsuzawa/tflow.git',
    author='Takumi',
    author_email='tmatsuzawa@uchicago.edu',
    description='tflow - a Python package to analyze 2D/3D (laminar/turbulent) velocity fields',
    packages=find_packages(),    
    install_requires=['numpy', 'matplotlib'],
)





