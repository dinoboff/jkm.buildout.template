from setuptools import setup, find_packages

setup(
    name = "jkm.paste.template",
    version = "1.0a3",
    url = '',
    license = 'BSD',
    description = "A buildout tamplate for PasteScript.",
    author = 'Damien Lebrun',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['jkm.paste'],
    install_requires=['setuptools', 'PasteScript', 'Cheetah'],
    entry_points="""
        # -*- Entry points: -*-
        [paste.paster_create_template]
        jkm_buildout = jkm.paste.template:BuildoutTemplate
        """
)

