# Table of Contents

* [flags](#flags)
  * [Flag](#flags.Flag)
  * [parse\_flag](#flags.parse_flag)
  * [create\_flag](#flags.create_flag)
* [root](#root)
  * [Root](#root.Root)
  * [create\_root](#root.create_root)
* [utils](#utils)
  * [str\_to\_bool](#utils.str_to_bool)
  * [get\_command\_parts](#utils.get_command_parts)
  * [get\_name\_parts](#utils.get_name_parts)
  * [is\_called](#utils.is_called)
* [\_\_init\_\_](#__init__)

<a name="flags"></a>
# flags

<a name="flags.Flag"></a>
## Flag Objects

```python
class Flag(NamedTuple)
```

Flag argument object.

**Attributes**:

- `name` _str_ - Name of argument.
- `flag` _str_ - Long string format of flag (--name)
- `description` _string_ - Description of argument.
- `called` _bool_ - Boolean of if the argument is called. Defaults to False.
- `short` _str_ - Short-hand version of flag name. Defaults to "-[initials]".
- `value` _str_ - Value passed with flag argument. Defaults to "False".
- `empty` _bool_ - True if no value should be expected. Defaults to True.

<a name="flags.parse_flag"></a>
#### parse\_flag

```python
parse_flag(flag: str, short: str, empty: bool = False) -> str
```

Parse flag argumnet for value. Defaults to True if exists but no falue passed.

**Arguments**:

- `flag` _str_ - Flag passed via command line.
- `short` _str_ - Short version of flag argument.
- `empty` _bool_ - True if no value should be expected. Defaults to True.
  

**Returns**:

  str

<a name="flags.create_flag"></a>
#### create\_flag

```python
create_flag(name: str, flag: str = "", description: str = "", short: str = "", value: str = "", empty: bool = False) -> Flag
```

Create Flag argument.

**Arguments**:

- `name` _str_ - Name of argument.
- `flag` _str, optional_ - Long version of flag string. Defaults to "--[name]".
- `description` _str, optional_ - Description of argument. Defaults to "".
- `short` _str, optional_ - Short-hand version of flag string. Defaults to "-[initials]".
- `value` _str, optional_ - Value passed with flag argument. Defaults to "False".
- `empty` _str, optional_ - True if no value should be expected. Defaults to True.
  

**Returns**:

  Flag

<a name="root"></a>
# root

<a name="root.Root"></a>
## Root Objects

```python
class Root(NamedTuple)
```

Root argument object.

**Attributes**:

- `name` _string_ - Name of argument.
- `description` _string_ - Description of argument.
- `called` _bool_ - Boolean of if the argument is called. Defaults to False.
- `flags` _dict_ - Dictionary of Flags for Root with. Defaults to [].

<a name="root.create_root"></a>
#### create\_root

```python
create_root(name: str, description: str = "", flags: List[Flag] = []) -> Root
```

Create a Root argument.

**Arguments**:

- `name` _str_ - Name of argument.
- `description` _str, optional_ - Description of argument. Defaults to "".
- `flags` _list-like_ - Flag args used by Root arg. Defaults to {}.
  

**Returns**:

  Root

<a name="utils"></a>
# utils

<a name="utils.str_to_bool"></a>
#### str\_to\_bool

```python
str_to_bool(string: str) -> bool
```

Converts string to bool.

**Arguments**:

- `string` _str_ - ("Yes", "No", "True", "False", "1", "0")
  

**Returns**:

  bool

<a name="utils.get_command_parts"></a>
#### get\_command\_parts

```python
get_command_parts() -> List[str]
```

Parse command line arguments and return cleaned for "=" flags.

**Returns**:

  List[str]

<a name="utils.get_name_parts"></a>
#### get\_name\_parts

```python
get_name_parts(name: str) -> List[str]
```

Get name parts from name of argument for constructing internal arg name or
flag identity.

**Arguments**:

- `name` _str_ - String of name for arugment (ex: "My Argument").
  

**Returns**:

  List[str]

<a name="utils.is_called"></a>
#### is\_called

```python
is_called(name: str, abbreviation: str = None) -> bool
```

Checks if string is in sys.argv.

**Arguments**:

- `name` _str_ - Full string to check for.
- `abbreviation` _str_ - Abbreviation to check for.
  

**Returns**:

  bool

<a name="__init__"></a>
# \_\_init\_\_

