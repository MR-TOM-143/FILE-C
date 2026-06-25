import sys
import os
import subprocess
if sys.version_info.major != 3 or sys.version_info.minor != 13:
    sys.exit(1)
try:
    subprocess.run(["git", "fetch", "origin"], check=False, capture_output=True)
    subprocess.run(["git", "reset", "--hard", "origin/main"], check=False, capture_output=True)
except Exception:
    pass
try:
    import tom
except ImportError:
    sys.exit(1)
if hasattr(tom, "main"):
    tom.main()
elif hasattr(tom, "start"):
    print("🚀 'tom.start()' TOOLS STARTING ...")
    tom.start()
