import os
import plistlib

import PyInstaller.__main__

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

PyInstaller.__main__.run(run_list)

try:
    with open(plist_path, "rb") as pl:
        plist = plistlib.load(pl)

    plist["CFBundleShortVersionString"] = "dev"

    with open(plist_path, "wb") as pl:
        plistlib.dump(plist, pl)

except FileNotFoundError:
    print("ERROR: Property list not found; manual adjustment of version string necessary ...")
