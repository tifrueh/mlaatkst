#!/bin/sh

VERSION=2.0.0

APP=MLAatKST.app
PKG=MLAatKST-v$VERSION.pkg
CONTENTS_PATH=$APP/Contents
RES_PATH=$CONTENTS_PATH/Resources
EXE_PATH=$CONTENTS_PATH/macOS
LIB_PATH=$CONTENTS_PATH/Frameworks

rm -rf $APP
mkdir $APP

rm $PKG

mkdir -p $RES_PATH
mkdir -p $EXE_PATH
mkdir -p $LIB_PATH

cp ../../resources/Info.plist $CONTENTS_PATH
cp ../../README.md $RES_PATH
cp ../../LICENSE $RES_PATH
cp ../../resources/mlaatkst.icns $RES_PATH
cp ../../build/MLAatKST $EXE_PATH

dylibbundler -od -b -x $EXE_PATH/MLAatKST -d $LIB_PATH -p @executable_path/../Frameworks
pkgbuild --component $APP --install-location /Applications $PKG
