application_title="LOL Queue Search | A Eco Community Project"
main_python_file="main.py"
include_files=["accept.png", "icon.png", "queue.png"]
your_name="Eco#0745"
program_description="A desktop application that can automatically accepted your League Of Legends match"

#main
import sys

from cx_Freeze import Executable, setup

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name=application_title,
    version="1.0",
    description=program_description,
    author=your_name,
    options={"build_exe": {"include_files": include_files}},
    executables=[Executable(main_python_file, base=base)]
)