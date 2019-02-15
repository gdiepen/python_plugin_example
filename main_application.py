from plugin_collection import PluginCollection


def main():
    my_plugins = PluginCollection('plugins')
    my_plugins.apply_all_plugins_on_value(5)



if __name__ == '__main__':
    main()
