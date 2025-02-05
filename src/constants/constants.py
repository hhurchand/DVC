import argparse
from constants import CONFIG
import yaml
from typing import Any, Dict

def get_config(config_path: str = CONFIG)-> Dict[str, Any]:
    """Reads the YAML configuration file and returns the project parameters

    Args:
        config_path (str, optional): Path to the parameter file. Defaults to "params.yaml".

    Returns:
        Dict[str, Any]: Dictionary containing project config
    """
    with open(config_path, 'r') as yaml_file:
        try:
            config = yaml.safe_load(yaml_file)
        except yaml.YAMLError as e:
            print(f"Error loading YAML file: {e}")
            return None
    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load configuration from YAML file")
    parser.add_argument("--config",default=CONFIG, help="Path to YAML configuration file")
    args = parser.parse_args()

    config = get_config(args.config)
    print("config",config["raw_data_config"]["raw_data"])

