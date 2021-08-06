"""Main application that demonstrates the functionality of
the dynamic plugins and the PluginCollection class
"""

from plugin_collection import PluginCollection

def main():
    """main function that runs the application
    """
    my_plugins = PluginCollection('plugins')
    my_plugins.apply_all_plugins_on_value(5)

if __name__ == '__main__':
    main()
