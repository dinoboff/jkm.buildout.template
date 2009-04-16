from setuptools import setup, find_packages

setup(
    name = "jkm.buildout.template",
    version = "1.0",
    url = '',
    license = 'BSD',
    description = "A buildout tamplate for PasteScript.",
    author = 'Damien Lebrun',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires=['setuptools', 'PasteScript'],
    entry_points="""
        # -*- Entry points: -*-
        [paste.paster_create_template]
        jkm_buildbout = jkm.buildout.template:BuildoutTemplate
        """
)

