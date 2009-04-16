from datetime import date
from paste.script.templates import var
from paste.script.templates import Template

YEAR = date.today().year

class BuildoutTemplate(Template):
    """Buildout template"""
    _template_dir = 'tmpl/buildout'
    summary = "A basic buildout layout"
    use_cheetah = True
    vars = [
        var('package', 'The package contained',
            default='example'),
        var('version', 'Version', default='0.1.0'),
        var('description',
            'One-line description of the package'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('org', 'Organisation name (for licence)'),
        ]
    def check_vars(self, vars, command):
        vars['year'] = YEAR
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return Template.check_vars(self, vars, command)