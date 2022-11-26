import argparse
from config_reader import ConfigReader

def main():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file_path", default="config.py")
    args = parser.parse_args()
    config = ConfigReader.read_config(args.config_file_path)
    main()