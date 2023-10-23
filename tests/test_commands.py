from yamlenv import load


def test_join():
    _s = """
    base_dir: &BASE_DIR "xyz/"
    some_dir: &SOME_DIR "abcd/efgh"
    new_dir: !join [*BASE_DIR, *SOME_DIR]
    """
    assert load(_s)["new_dir"] == "xyz/abcd/efgh"
    assert not load(_s)["new_dir"] == "xyz/abcd/efg"


def test_substr():
    _s = """
    some_dir: &SOME_DIR "abcd/efgh"
    new_dir: !substr [*SOME_DIR, 0, 4]
    """
    assert load(_s)["new_dir"] == "abcd"


def test_replace():
    _s = """
    some_dir: &SOME_DIR "abcd/efgh"
    new_dir: !replace [*SOME_DIR, ef, xy]
    """
    assert load(_s)["new_dir"] == "abcd/xygh"
