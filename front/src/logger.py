import logging

from pathlib import Path

class ShopLogger:

    def __init__(self, name:str, level=logging.INFO) -> None:
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(level)

        self.dir_path = Path('log')
        self.dir_path.mkdir(parents=True, exist_ok=True)

        handler = logging.FileHandler(f"log//{self.name}.log")
        handler.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def log_info(self, message):
            self.logger.info(message)

