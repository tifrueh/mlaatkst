#!/bin/sh

parent_path=$( cd "$(dirname "$0")" ; pwd -P )

cd "$parent_path"


APP=MLAatKST.app
CONTENTS_PATH=$APP/Contents
RES_PATH=$CONTENTS_PATH/Resources
EXE_PATH=$CONTENTS_PATH/macOS
LC_DE_PATH=$RES_PATH/de.lproj

rm -rf $APP
mkdir $APP

mkdir -p $RES_PATH
mkdir -p $EXE_PATH
mkdir -p $LC_DE_PATH

cp ../../resources/Info.plist $CONTENTS_PATH
cp ../../README.md $RES_PATH
cp ../../LICENSE $RES_PATH
cp ../../resources/mlaatkst.icns $RES_PATH
cp ../../build/MLAatKST $EXE_PATH
cp ../../resources/lang/de/LC_MESSAGES/mlaatkst.mo $LC_DE_PATH
cp ../../resources/lang/de/LC_MESSAGES/wxstd.mo $LC_DE_PATH
