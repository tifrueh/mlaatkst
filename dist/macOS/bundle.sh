#!/bin/sh

parent_path=$( cd "$(dirname "$0")" ; pwd -P )

cd "$parent_path"

VERSION=2.1.0-dev

APP=MLAatKST.app
PKG=MLAatKST-macOS-universal-v$VERSION.pkg
CONTENTS_PATH=$APP/Contents
RES_PATH=$CONTENTS_PATH/Resources
EXE_PATH=$CONTENTS_PATH/macOS
LIB_PATH=$CONTENTS_PATH/Frameworks
LC_DE_PATH=$RES_PATH/de.lproj

rm -rf $APP
mkdir $APP

rm $PKG

mkdir -p $RES_PATH
mkdir -p $EXE_PATH
mkdir -p $LIB_PATH
mkdir -p $LC_DE_PATH

cp ../../resources/Info.plist $CONTENTS_PATH
cp ../../README.md $RES_PATH
cp ../../LICENSE $RES_PATH
cp ../../resources/mlaatkst.icns $RES_PATH
cp ../../build/MLAatKST $EXE_PATH
cp ../../resources/lang/de/LC_MESSAGES/mlaatkst.mo $LC_DE_PATH

productbuild --component $APP /Applications $PKG

rm -rf $APP
