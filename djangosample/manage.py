#!/usr/bin/env python
import os
import sys
import os
from collections import *
import sys





if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosample.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
