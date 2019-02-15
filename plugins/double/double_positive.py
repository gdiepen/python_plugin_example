from plugin_collection import Plugin

class DoublePositive:
    """This plugin will just multiply the argument with the value 2
    """

    def perform_operation(self, argument):
        """The actual implementation of this plugin is to multiple the
        value of the supplied argument by 2
        """
        return argument*2
