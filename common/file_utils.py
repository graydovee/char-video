import os
import pickle
import re


def find_file(target_dir, prefix):
    if os.path.exists(target_dir) and os.path.isdir(target_dir):
        for file in os.listdir(target_dir):
            if file.startswith(prefix):
                return file
    return None


def deep_find_files(target_dir, pattern, flags=0):
    match_list = []
    if isinstance(target_dir, list):
        for each in target_dir:
            match_list += deep_find_files(each, pattern)
        return match_list
    elif isinstance(target_dir, str):
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            for file in os.listdir(target_dir):
                full_path = os.path.join(target_dir, file)
                if os.path.isdir(full_path):
                    match_list += deep_find_files(full_path, pattern)
                elif not (re.match(pattern, file, flags) is None):
                    match_list.append(full_path)
        return match_list


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
