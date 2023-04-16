# pygedcom

Python module to parse GEDCOM 5.5.1 files and generate output files in a more human readable format.

Full documentation is available at [https://topetit.github.io/pygedcom/docs/](https://topetit.github.io/pygedcom/docs/).


## Installation

You can install the module with pip:

```bash
pip install pygedcom
```

## Getting started

First, you need to import the `pygedcom` module.

```python
import pygedcom
```


To get started with the `parser` module, you'll need to initialize a `GedcomParser` object:


```python
parser = pygedcom.GedcomParser(path="path/to/your/gedcom_file.ged")
```

You can check the parsing statistics to ensure that you've parsed the file correctly:


```python
print(parser.get_stats())
```

It's good practice to verify your GEDCOM file before parsing it. You can do this with the following command:


```python
check = parser.verify()
if check.status == 'ok':
    print("Your GEDCOM file is valid")
else:
    print("Your GEDCOM file is not valid")
    print(check.errors)
```

Here is the full setup block:

```python
import pygedcom

parser = pygedcom.GedcomParser(path="path/to/your/gedcom_file.ged")
check = parser.verify()

if check.status == 'ok':
    print("Your GEDCOM file is valid")
else:
    print("Your GEDCOM file is not valid")
    print(check.errors)

print(parser.get_stats())
```

## Parsing


The parser is a simple recursive parser. It creates a series of `GedcomElement` objects.

```python
    # Initialize the parser
    data = parser.parse()
```

Now the `data` object contains the parsed data. This is a dictionary with the following fields:
- **head**: the `GedcomHead` object.
- **submitters**: a list of `GedcomSubmitter` objects.
- **individuals**: a list of `GedcomIndividual` objects.
- **families**: a list of `GedcomFamily` objects.
- **objects**: a list of `GedcomObject` objects.
- **notes**: a list of `GedcomNote` objects.
- **repository**: a list of `GedcomRepository` objects.
- **source**: a list of `GedcomSource` objects.


## Export

The export function is used to export the GedcomParser object to a file. The export function takes two arguments:

- **format** (str): The format to export to. Currently only "json" is supported.
- **empty_fields** (bool): Whether to include empty fields in the export. Defaults to True.

This is a recursive export process. The method `GedcomParser.export()` calls the `GedcomElement.export()` method for each element in the GedcomParser object. All attributes starting with `__export_` are exported.
This is implemented as such to centralise the export process and to make it easy to add new export formats. Only one declaration is needed in the `GedcomElement`. If you want an attribute to be exported, you need it to start with `__export_`.

```python
# Make sure you initialized the parser first
parser = GedcomParser("path/to/file.ged")
parser.parse()
export = parser.export("json", empty_fields=False)

# Write the export to a file
with open("path/to/export.json", "w") as f:
    f.write(export)
```

The `export` variable in this example contains the exported GedcomParser object as a string. You can write this string to a file or do whatever you want with it.
