#!/bin/bash
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR/src" || exit

pyinstaller --clean --name="MLAatKST" --windowed \
  --icon="$SCRIPT_DIR/assets/mlaatkst.icns" \
  --osx-bundle-identifier="com.tifrueh.mlaatkst" \
  --add-data="$SCRIPT_DIR/README.md:." \
  --add-data="$SCRIPT_DIR/LICENSE.md:." \
  --add-data="$SCRIPT_DIR/src/resources/bg2.png:./resources" \
  --add-data="$SCRIPT_DIR/src/resources/lang.txt:./resources" \
  --workpath="$SCRIPT_DIR/out/build" \
  --distpath="$SCRIPT_DIR/out/dist" \
  "$SCRIPT_DIR/src/main.py" &&

plutil -replace "CFBundleShortVersionString" -string "1.2.1" "$SCRIPT_DIR/out/dist/MLAatKST.app/Contents/Info.plist"
