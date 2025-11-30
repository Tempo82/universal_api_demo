import os
import json

class StorageManager:
    def __init__(self, base_dir="./demo_storage"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def save_file(self, app_name, file_name, data):
        app_dir = os.path.join(self.base_dir, app_name)
        os.makedirs(app_dir, exist_ok=True)
        path = os.path.join(app_dir, file_name)
        with open(path, "w") as f:
            json.dump(data, f)
        return path