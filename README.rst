Python Tools for Setting up Logging
-----------------------------------
Usage

.. code-block:: python

   import logging
   from loggingtools import setup_logging
   setup_logging('logging.yaml')
   logger = logging.getLogger('<package_name>')
   ...
