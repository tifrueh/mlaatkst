#!/bin/sh

APP=MLAatKST.app
CONTENTS_PATH=$APP/Contents
RES_PATH=$CONTENTS_PATH/Resources
EXE_PATH=$CONTENTS_PATH/macOS
LIB_PATH=$CONTENTS_PATH/Libraries

rm -rf $APP
mkdir $APP

mkdir -p $RES_PATH
mkdir -p $EXE_PATH
mkdir -p $LIB_PATH

cp ../../resources/Info.plist $CONTENTS_PATH
cp ../../README.md $CONTENTS_PATH
cp ../../resources/mlaatkst.icns $RES_PATH
cp ../../build/MLAatKST $EXE_PATH

dylibbundler -od -b -x $EXE_PATH/MLAatKST -d $LIB_PATH -p @executable_path/../Libraries
