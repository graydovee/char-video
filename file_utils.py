import os
import pickle


def find_file(target_dir, prefix):
    if os.path.exists(target_dir) and os.path.isdir(target_dir):
        for file in os.listdir(target_dir):
            if file.startswith(prefix):
                return file
    return None


def remove_all(path):
    if os.path.exists(path) and os.path.isdir(path):
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            os.remove(full_path)


def save(bean, file):
    with open(file, "wb") as f:
        pickle.dump(bean, f)


def load(file):
    try:
        if os.path.exists(file):
            with open(file, "rb") as f:
                return pickle.load(f)
    except:
        return None
