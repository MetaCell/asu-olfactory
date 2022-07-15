#!/usr/bin/env python3

from cloudharness.utils.server import init_flask, main


app = init_flask(title="Olphactory pubchem index API", webapp=False)

if __name__ == '__main__':
    main()
