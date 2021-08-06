"""Negative double function
"""

from plugin_collection import Plugin

class DoubleNegative(Plugin):
    """This plugin will just multiply the argument with the value -2
    """
    # pylint: disable=too-few-public-methods

    def __init__(self):
        super().__init__()
        self.description = 'Negative double function'

    def perform_operation(self, argument):
        """The actual implementation of this plugin is to multiple the
        value of the supplied argument by -2
        """
        return argument*-2
