Getting started
===============

First, you need to import the `gedcom_parser` module.

.. code-block:: python

    import pygedcom


To get started with the `gedcom_parser` module, you'll need to initialize a `GedcomParser` object:

.. code-block:: python

    parser = pygedcom.GedcomParser(path="path/to/your/gedcom_file.ged")

You can check the parsing statistics to ensure that you've parsed the file correctly:

.. code-block:: python

    print(parser.get_stats())

It's a good practice to verify your GEDCOM file before parsing it. You can do this with the following command:

.. code-block:: python

    verif = parser.verify()
    if verif.status == 'ok':
        print("Your GEDCOM file is valid")
    else:
        print("Your GEDCOM file is not valid")
        print(verif.errors)


Here is the full setup block:

.. code-block:: python

    import pygedcom

    parser = pygedcom.GedcomParser(path="path/to/your/gedcom_file.ged")
    verif = parser.verify()
    if verif.status == 'ok':
        print("Your GEDCOM file is valid")
    else:
        print("Your GEDCOM file is not valid")
        print(verif.errors)

    print(parser.get_stats())
