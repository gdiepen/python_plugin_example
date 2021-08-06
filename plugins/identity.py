"""Identity function
"""

from plugin_collection import Plugin

class Identity(Plugin):
    """This plugin is just the identity function: it returns the argument
    """
    # pylint: disable=too-few-public-methods

    def __init__(self):
        super().__init__()
        self.description = 'Identity function'

    def perform_operation(self, argument):
        """The actual implementation of the identity plugin is to just return the
        argument
        """
        return argument
