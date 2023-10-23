import typing as T
import yaml
from yaml.error import YAMLError
from yamlenv import env, loader
from yamlenv.types import Stream


__version__ = "0.7.1"


def join(_loader, node):
    seq = _loader.construct_sequence(node)
    return "".join([str(i) for i in seq])


def substr(_loader, node):
    _data = _loader.construct_sequence(node)
    try:
        assert len(_data) == 3
    except AssertionError:
        raise YAMLError(f"need 3 arguments, got {len(_data)}")
    return _data[0][_data[1]: _data[2]]


def replace(_loader, node):
    _data = _loader.construct_sequence(node)
    try:
        assert len(_data) == 3
    except AssertionError:
        raise YAMLError(f"need 3 arguments, got {len(_data)}")
    return str(_data[0]).replace(str(_data[1]), str(_data[2]))


def load(stream):
    # type: (Stream) -> T.Any
    yaml.add_constructor("!join", join, loader.Loader)
    yaml.add_constructor("!substr", substr, loader.Loader)
    yaml.add_constructor("!replace", replace, loader.Loader)
    data = yaml.load(stream, loader.Loader)
    return env.interpolate(data)


def load_all(stream):
    # type: (Stream) -> T.Iterator[T.Any]
    for data in yaml.load_all(stream, loader.Loader):
        yield env.interpolate(data)
