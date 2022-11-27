import argparse
import json

def main(config):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file_path", default="configs/config.py")
    args = parser.parse_args()
    with open(args.config_file_path, "r") as file:
        config = json.load(file)
    main(config)