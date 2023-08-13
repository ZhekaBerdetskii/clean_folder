from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_bev',
    version='1.0',
    description='Clean folder',
    author='Berdetskii Yevgeniy',
    author_email='testbev@examle.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
)