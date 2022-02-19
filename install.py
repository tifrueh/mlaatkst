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

PyInstaller.__main__.run([
    "--clean",
    "--windowed",
    f"--name={name}",
    f"--icon={icon_path}",
    f"--osx-bundle-identifier={osx_bundle_identifier}",
    f"--add-data={readme_path}:.",
    f"--add-data={license_path}:.",
    f"--add-data={resources_path}:resources",
    f"--workpath={workpath}",
    f"--distpath={distpath}",
    "--noupx",
    f"{main_path}",
    "-y"
])

try:
    with open(plist_path, "rb") as pl:
        plist = plistlib.load(pl)

    plist["CFBundleShortVersionString"] = "dev"

    with open(plist_path, "wb") as pl:
        plistlib.dump(plist, pl)

except FileNotFoundError:
    print("ERROR: Property list not found; manual adjustment of version string necessary ...")
