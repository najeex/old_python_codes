import os
import sys

try:
    os.mkdir("newdir")

    print('directory created')

    raise RuntimeError("Runtime error accourred")

except (FileExistsError, RuntimeError) as e:
    print(e)
