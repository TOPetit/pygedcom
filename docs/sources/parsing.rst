Parsing
=======

The parser is a simple recursive parser. It creates a series of `GedcomElement` objects.

.. code-block:: python

    # Initialize the parser
    data = parser.parse()

Now the `data` object contains the parsed data. This is a dictionary with the following fields:
    - **head**: the :class:`GedcomHead` object.
    - **submitters**: a list of :class:`GedcomSubmitter` objects.
    - **individuals**: a list of :class:`GedcomIndividual` objects.
    - **families**: a list of :class:`GedcomFamily` objects.
    - **objects**: a list of :class:`GedcomObject` objects.
    - **notes**: a list of :class:`GedcomNote` objects.
    - **repository**: a list of :class:`GedcomRepository` objects.
    - **source**: a list of :class:`GedcomSource` objects.
