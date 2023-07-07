#!/bin/sh

parent_path=$( cd "$(dirname "$0")" ; pwd -P )

cd "$parent_path"

echo "----=SIGNING=----"

codesign --force --verbose=2 --sign $CERT_APPL --options runtime MLAatKST.app

echo "-----------------\n"

echo "---=VERIFYING=---"

codesign --verbose=2 --verify MLAatKST.app

echo "-----------------\n"
