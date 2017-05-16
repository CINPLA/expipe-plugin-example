from expipecli.utils import IPlugin
import click


class MyPlugin(IPlugin):
    """Create the `expipe do-incredible-stuff` command."""
    def attach_to_cli(self, cli):
        @cli.command('do-incredible-stuff')
        @click.argument('stuff', type=click.STRING)
        def incredible(stuff):
            '''
            Do incredible stuff

            COMMAND: stuff
            '''

            print('incredible', stuff)
