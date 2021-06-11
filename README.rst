|image0| |image1| |image2|

Python Tio SDK
=================

Homemade SDK for `tio.run <https://tio.run>`__

Developed and used for `tuxbot-bot <https://github.com/Rom1-J/tuxbot-bot>`__

Installing the pre-requirements
-------------------------------

-  The pre-requirements are:

   -  Python 3.8 or greater
   -  Pip
   -  Git


Examples
--------

Some examples:

Sync
^^^^

.. code-block:: python

    >>> from tio.tio import Tio
    >>>
    >>> tio = Tio()
    >>> tio.get_languages().keys()
    dict_keys(['05ab1e', '1l-a', '1l-aoi', '2dfuck', '2l', '2sable'...
    >>>
    >>> print(tio.run("python", "print(42)"))
    42

    Exit code: 0

Async
^^^^^

.. code-block:: python

    >>> from tio.tio import AsyncTio
    >>> import asyncio
    >>>
    >>> async def main():
    ...    tio = AsyncTio()
    ...    print((await tio.get_languages()).keys())
    ...    print(await tio.run("python", "print(42)"))
    >>>
    >>> asyncio.run(main())
    dict_keys(['05ab1e', '1l-a', '1l-aoi', '2dfuck', '2l', '2sable'...
    42

    Exit code: 0


.. |image0| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-%23007ec6
.. |image1| image:: https://img.shields.io/github/issues/Rom1-J/tuxbot-bot
.. |image2| image:: https://img.shields.io/badge/code%20style-black-000000.svg
