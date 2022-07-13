import sys
from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="guifoo",
      version="0.1",
      description="My GUI application!",
      options={"build_exe": {"include_files": [
          "artworks/", "sounds/", "fonts/"]}},
      executables=[Executable("main.py", base=base)])
