import plugin_collection

class DoubleNegative(plugin_collection.Plugin):
    """This plugin will just multiply the argument with the value -2
    """
    def __init__(self):
        super().__init__()
        self.description = 'Negative double function'

    def perform_operation(self, argument):
        """The actual implementation of this plugin is to multiple the
        value of the supplied argument by -2
        """
        return argument*-2
