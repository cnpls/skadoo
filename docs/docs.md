# Table of Contents

* [main](#main)
  * [is\_called](#main.is_called)
  * [Flag](#main.Flag)
  * [create\_flag](#main.create_flag)
  * [Root](#main.Root)
  * [create\_root](#main.create_root)
* [utils](#utils)
  * [str\_to\_bool](#utils.str_to_bool)
* [\_\_init\_\_](#__init__)

<a name="main"></a>
# main

<a name="main.is_called"></a>
#### is\_called

```python
is_called(string: str) -> bool
```

Checks if string is in sys.argv.

**Arguments**:

- `string` _str_ - String to check for.
  

**Returns**:

  bool

<a name="main.Flag"></a>
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

<a name="main.create_flag"></a>
#### create\_flag

```python
create_flag(name: str, flag: str = "", description: str = "", short: str = "", value: str = "") -> Flag
```

Create Flag argument.

**Arguments**:

- `name` _str_ - Name of argument.
- `flag` _str, optional_ - Long version of flag string. Defaults to "--[name]".
- `description` _str, optional_ - Description of argument. Defaults to "".
- `short` _str, optional_ - Short-hand version of flag string. Defaults to "-[initials]".
- `value` _str, optional_ - Value passed with flag argument. Defaults to "False".
  

**Returns**:

  Flag

<a name="main.Root"></a>
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

<a name="main.create_root"></a>
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

<a name="__init__"></a>
# \_\_init\_\_

