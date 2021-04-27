import json
import os
import pathlib
import yaml


PLUGINS_DIR = "plugins"
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PLUGIN_DATA_FILE = "plugin.yaml"


class Constants:
    OutFile = "catalog"
    OutputFormatJson = "json"
    OutputFormatYaml = "json"


def get_plugins_path():
    return os.path.join(PROJECT_PATH, PLUGINS_DIR)


def gather_plugin_directories(path):
    return [
        os.path.join(path, obj) for obj in os.listdir(path) if os.path.isdir(os.path.join(path, obj))
    ]


def load_plugin_yaml(plugin_directory, should_raise=False):
    plugin_data_path = os.path.join(plugin_directory, PLUGIN_DATA_FILE)
    if not pathlib.Path(plugin_data_path).exists():
        if should_raise:
            raise FileNotFoundError(plugin_data_path)
        return None
    return yaml.load(open(plugin_data_path, 'r').read(), Loader=yaml.Loader)


def write_outfile(data, filename=Constants.OutFile, output_format=Constants.OutputFormatJson):
    full_filename = "%s.%s" % (filename, output_format)
    with open(full_filename, 'w') as outfile:
        if output_format == Constants.OutputFormatJson:
            json.dump(data, outfile, indent=4)
        elif output_format == Constants.OutputFormatYaml:
            yaml.dump(data, outfile)
        else:
            raise ValueError("Output format %s not supported." % output_format)
    return filename


if __name__ == "__main__":
    print("HERE WE GO")
    plugins_dir_path = get_plugins_path()
    plugin_directories = gather_plugin_directories(plugins_dir_path)
    plugins_data = [
        load_plugin_yaml(plugin_dir, should_raise=True) for plugin_dir in plugin_directories
    ]
    write_outfile(plugins_data)
