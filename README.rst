orm_gen
---------

generate sqlalchemy orm class automatically from existing database tables

- easy to use and extend
- support column table
- support composite index, besides composite primary key

Usage:
------

::

  ormgen --help:


  usage: ormgen [--help] [-v] [-h HOST] [-u USER] [-p PASSWORD] [-s SCHEMA]
              [-o OUTFILE]

  Generates SQLAlchemy model code from an existing database.

  optional arguments:
    --help                show help
    -v, --version         show version
    -h HOST, --host HOST  mysql host
    -u USER, --user USER  username
    -p PASSWORD, --password PASSWORD
                        password
    -s SCHEMA, --schema SCHEMA
                        schema
    -o OUTFILE, --outfile OUTFILE
                          file to write output to (default: stdout)
