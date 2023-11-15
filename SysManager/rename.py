import datetime
import os
import time

import VARS
from SysManager.systems_check import log_text

s = time.time()


def b_rename(directory):
    current_month_year = datetime.datetime.now().strftime("%m%Y")
    i = 1

    for filename in os.listdir(directory):
        new_name = f"{current_month_year}-models-{i}"
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        os.rename(old_file, new_file)
        i += 1


# Usage example
directory = VARS.music
b_rename(directory)
log_text(f"Elapsed time: {time.time() - s}", "../logs/rename_log.txt")
