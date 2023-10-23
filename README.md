#### YAMLENV

This is a fork of [Ibolla/yamlenv](https://github.com/lbolla/yamlenv.git) that I added some stuff to.

If you want the original package, you can pip install it from pypi using `yamlenv`, for this package you should use `yamlenv2`.

As in the original package, you can interpolate environment variables using this package, i.e., you can write stuff like `loc: ${HOME}/x/y/z` in your yml file and read that file with `yamlenv.load(a.yml)` and loc will be interpolated to your `${HOME}` environment variable.

I have added some methods that I find useful
- `join`: joins a sequence of strings.
```yaml
some_dir: &SOME_DIR "abcd/efgh"
new_dir: !join ["${HOME}/", *SOME_DIR]
```

- `replace`: replace strings, syntax: `(string_to_operate_on, string_to_replace, string_to_replace_with)`
```yaml
some_val: &SOME_VAL some-thing
some_other_val: &SOME_OTHER_VAL some-other-thing
file_name: &FILE_NAME !join [ !replace [*SOME_VAL, "-", "_"], "-", !replace [*SOME_OTHER_VAL, "-", "_"]]
```

- `substr`: sub string: syntax: `(string_to_operate_on, start_index, end_index)`
```yaml
some_val: &SOME_VAL some-thing
some_other_val: &SOME_OTHER_VAL some-other-thing
file_name: &FILE_NAME !join [ !replace [*SOME_VAL, "-", "_"], "-", !replace [*SOME_OTHER_VAL, "-", "_"]]
```
