import os
import subprocess
import sys
import time

sys.argv.pop(0)

pandaDir = os.environ.get("PANDA_PATH_1") + "\\bin\\" if os.environ.get("PANDA_PATH_1") else ""
print(f"Panda Directory = {pandaDir}")

for entry in sys.argv:
    if entry.endswith(".bam"):
        subprocess.call([f"{pandaDir}bam2egg.exe", entry, '-o', entry.replace('.bam', '.egg')])
    # Give some time for the user to see the output before closing
    time.sleep(3)

