<h1 align="center">ToyBase 🚂</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Sas2k/ToyBase.svg)](https://github.com/Sas2k/ToyBase/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Sas2k/ToyBase.svg)](https://github.com/Sas2k/ToyBase/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

<p align="center"> A Toy Database System written in Python
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 Getting Started ](#-getting-started-)
  - [First off, Installing](#first-off-installing)
  - [And that's it basically...](#and-thats-it-basically)
- [🎈 Usage ](#-usage-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)

## 🧐 About <a name = "about"></a>

This is a simple Toy Database System written in Python. It's not meant to be used in production but you can use it in a small apps if ou want. This is meant as a learning tool for people who want to learn how databases work. it's fairly simple to learn and use.

## 🏁 Getting Started <a name = "getting_started"></a>

### First off, Installing

just use pip.

```bash
$ pip install ToyBase
```

### And that's it basically...

## 🎈 Usage <a name="usage"></a>

Creating a new table.

```python
from ToyBase import ToyBase

base = ToyBase("test")

base.create_table(["Name", "Phone"])
```

> This will create a new file called "test.tb" in the current directory.

Adding records/rows to the table.

```python
base.add_record(["John Doe", "123456789"])
```

> This will add a new record to the table.

Getting all records/rows from the table.

```python
base.show_records()
```

> This will return a list of all the records in the table.

Getting a specific record/row from the table.

```python
base.get_record(0)
```

> This will return the first record in the table.

Deleting a record/row from the table.

```python
base.delete_record(0)
```

> This will delete the first record in the table.


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming Language
- [Pickle](https://docs.python.org/3/library/pickle.html) - Python Object Serialization

## ✍️ Authors <a name = "authors"></a>

- [@Sas2k](https://github.com/Sas2k) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.
