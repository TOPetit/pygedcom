Export
======

The export function is used to export the GedcomParser object to a file. The export function takes two arguments:

    - **format** (str): The format to export to. Currently only "json" is supported.
    - **empty_fields** (bool): Whether to include empty fields in the export. Defaults to True.

This is a recursive export.

.. code-block:: python

    # Make sure you initialized the parser first
    parser = GedcomParser("path/to/file.ged")
    parser.parse()
    export = parser.export("json", empty_fields=False)

    # Write the export to a file
    with open("path/to/export.json", "w") as f:
        f.write(export)

The `export` variable in this example contains the exported GedcomParser object as a string. You can write this string to a file or do whatever you want with it.
