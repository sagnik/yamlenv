from typing import List, Tuple, Mapping
import yaml


def write_file(data, path, mode="w", **kwargs):
    with open(path, mode=mode, **kwargs) as f:
        f.write(data)


def rec_val_replace(obj, replacements: List[Tuple[str, str]]):
    if isinstance(obj, Mapping):
        return {key: rec_val_replace(val, replacements)
                for key, val in obj.items()}
    elif isinstance(obj, str):
        for to_replace, replace_with in replacements:
            obj = obj.replace(to_replace, replace_with)
        return obj
    return obj


def replace_dump(data, path, replacements: List[Tuple[str, str]] = []):
    """
    dumps with replacements
    :param data:
    :param path:
    :param replacements:
    :return:
    """
    if not replacements:
        yaml.safe_dump(data, open(path, 'w'), default_flow_style=False)
        return
    data = rec_val_replace(data, replacements)
    yaml.safe_dump(data, open(path, 'w'),  default_flow_style=False, sort_keys=False)
    return
