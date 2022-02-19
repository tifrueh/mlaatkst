import argparse
import pathlib
import plistlib

import PyInstaller.__main__

# initialise parser
parser = argparse.ArgumentParser()

# add argument for universal2 compilation
parser.add_argument(
    "--universal2",
    help="build the app as universal2 binary (only works if python itself was compiled as universal2)",
    action="store_true"
)

# add argument for version string adjustment
parser.add_argument(
    "--version",
    help="change the version string of the final executable",
    type=str,
    default="HEAD"
)

# parse arguments
args = parser.parse_args()

# get path of the containing folder
dir_path = pathlib.PurePath(__file__).parent

# set some settings and paths for pyinstaller
name = "MLAatKST"
osx_bundle_identifier = "com.tifrueh.mlaatkst"
icon_path = dir_path.joinpath("assets", "mlaatkst.icns")
readme_path = dir_path.joinpath("README.md")
license_path = dir_path.joinpath("LICENSE.md")
resources_path = dir_path.joinpath("resources")
workpath = dir_path.joinpath("out", "build")
distpath = dir_path.joinpath("out", "dist")
main_path = dir_path.joinpath("mlaatkst", "__main__.py")
plist_path = distpath.joinpath("MLAatKST.app", "Contents", "Info.plist")

# create list to contain all pyinstaller arguments
run_list = list()

# add pyinstaller arguments to run_list
run_list.append("--clean")
run_list.append("--windowed")
run_list.append("--noupx")
run_list.append("-y")
run_list.append(f"--name={name}")
run_list.append(f"--icon={icon_path}")
run_list.append(f"--osx-bundle-identifier={osx_bundle_identifier}")
run_list.append(f"--add-data={readme_path}:.")
run_list.append(f"--add-data={license_path}:.")
run_list.append(f"--add-data={resources_path}:resources")
run_list.append(f"--workpath={workpath}")
run_list.append(f"--distpath={distpath}")
run_list.append(f"{main_path}")

# only add universal2 compilation flat if the argument was given
if args.universal2:
    run_list.append("--target-arch=universal2")

# run pyinstaller with run_list as arguments
PyInstaller.__main__.run(run_list)

# adjust version string in the property list of the final executable
try:
    with open(plist_path, "rb") as pl:
        print("INFO: Load property list for version string modification ...")
        plist = plistlib.load(pl)

    plist["CFBundleShortVersionString"] = args.version

    with open(plist_path, "wb") as pl:
        print("INFO: Rewrite property list after version string modification ...")
        plistlib.dump(plist, pl)

except FileNotFoundError:
    print("ERROR: Property list not found; manual adjustment of version string necessary ...")
