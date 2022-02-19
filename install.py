import os
import plistlib
import argparse

import PyInstaller.__main__

parser = argparse.ArgumentParser()

parser.add_argument(
    "--universal2",
    help="build the app as universal2 binary (only works if python itself was compiled as universal2)",
    action="store_true"
)

parser.add_argument(
    "--version",
    help="change the version string of the final executable",
    type=str,
    default="HEAD"
)

args = parser.parse_args()

dir_path = os.path.abspath(os.path.dirname(__file__))

name = "MLAatKST"
icon_path = os.path.join(dir_path, "assets", "mlaatkst.icns")
osx_bundle_identifier = "com.tifrueh.mlaatkst"
readme_path = os.path.join(dir_path, "README.md")
license_path = os.path.join(dir_path, "LICENSE.md")
resources_path = os.path.join(dir_path, "resources")
workpath = os.path.join(dir_path, "out", "build")
distpath = os.path.join(dir_path, "out", "dist")

main_path = os.path.join(dir_path, "mlaatkst/__main__.py")

plist_path = os.path.join(distpath, "MLAatKST.app", "Contents", "Info.plist")

run_list = list()

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

if args.universal2:
    run_list.append("--target-arch=universal2")

PyInstaller.__main__.run(run_list)

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
