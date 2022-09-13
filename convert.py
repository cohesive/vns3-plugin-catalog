import argparse
import json
import os
import pathlib
import yaml

from datetime import datetime
from typing import List, Dict


PLUGINS_DIR = "plugins"
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PLUGIN_DATA_FILE = "plugin.yaml"
CUR_BRANCH = os.environ.get("BRANCH", "master")
GITHUB_RAW_CONTENT_REPO_URL = "https://raw.githubusercontent.com/cohesive/vns3-plugin-catalog/%s" % CUR_BRANCH


class Constants:
    OutFile = "catalog"
    OutputFormatJson = "json"
    OutputFormatYaml = "json"


def log(message):
    print("[%s] [%s]" % (datetime.utcnow().isoformat()[:-3], message))


def get_plugins_path():
    return os.path.join(PROJECT_PATH, PLUGINS_DIR)


def gather_plugin_directories(path) -> List[str]:
    """Get list of directories for plugins

    Args:
        path (str): path to plugins directory

    Returns:
        List[str]
    """
    return [
        os.path.join(path, obj) for obj in os.listdir(path) if os.path.isdir(os.path.join(path, obj))
    ]


def load_plugin_yaml(plugin_directory, should_raise=False) -> Dict:
    """Load plugin's yaml file from directory.
    
    Raise FileNotFoundError if no file found.

    Args:
        plugin_directory (str]): path to plugin dir
        should_raise (bool, optional)

    Raises:
        FileNotFoundError:

    Returns:
        Dict
    """
    plugin_data_path = os.path.join(plugin_directory, PLUGIN_DATA_FILE)
    if not pathlib.Path(plugin_data_path).exists():
        if should_raise:
            raise FileNotFoundError(plugin_data_path)
        return None

    plugin_dict = yaml.load(open(plugin_data_path, 'r').read(), Loader=yaml.Loader)
    if plugin_dict.get('logo'):
        logo_path = plugin_dict['logo']
        if not logo_path.startswith('http'):
            plugin_dir_name = plugin_directory.split('/')[-1].rstrip('/')
            logo_url = "{base_url}/plugins/{plugin_dir}/{logo_file}".format(
                base_url=GITHUB_RAW_CONTENT_REPO_URL,
                plugin_dir=plugin_dir_name,
                logo_file=logo_path.lstrip('/')
            )

            plugin_dict['logo'] = logo_url

    if plugin_dict.get('description'):
        plugin_dict['description'] = plugin_dict['description'].strip()

    plugin_dict['id'] = plugin_dict['name'].lower().replace(' ', '-')

    return plugin_dict



def write_outfile(data, filename=Constants.OutFile, output_format=Constants.OutputFormatJson):
    """Write data as output format to file

    Args:
        data (dict): data to write
        filename (str, optional): defaults to catalog.[format]
        output_format (str, optional): json or yaml. defaults to json

    Raises:
        ValueError: [description]

    Returns:
        [type]: [description]
    """
    full_filename = "%s.%s" % (filename, output_format)
    with open(full_filename, 'w') as outfile:
        if output_format == Constants.OutputFormatJson:
            json.dump(data, outfile, indent=4)
        elif output_format == Constants.OutputFormatYaml:
            yaml.dump(data, outfile)
        else:
            raise ValueError("Output format %s not supported." % output_format)
    return filename


def get_arg_parser():
    parser = argparse.ArgumentParser(
        description='Plugin data JSON converter CLI',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
        Convert plugin repository data to valid JSON data model.
        """
    )

    parser.add_argument('-o', '--outfile', help='outfile name without the suffix. Suffix determined by format', dest='output_file', type=str, default='catalog')
    parser.add_argument('-f', '--format', dest='output_format', help='Output format: json or yaml', type=str, default='json')

    return parser


if __name__ == "__main__":
    parser = get_arg_parser()
    parsed_args = vars(parser.parse_args())
    log("Starting gather plugins")
    plugins_dir_path = get_plugins_path()
    log("Reading plugins from %s" % plugins_dir_path)
    plugin_directories = gather_plugin_directories(plugins_dir_path)
    log("Found %d plugin directories" % (len(plugin_directories)))
    all_plugins_data = [
        load_plugin_yaml(plugin_dir, should_raise=True) for plugin_dir in plugin_directories
    ]
    plugins_data = [
        plugin for plugin in all_plugins_data
        if not plugin.get('draft') 
    ]
    output_file = parsed_args["output_file"]
    output_format = parsed_args["output_format"]
    log("Writing output to file %s.%s" % (output_file, output_format))
    write_outfile(plugins_data, filename=output_file, output_format=output_format)
