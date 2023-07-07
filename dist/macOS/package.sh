#!/bin/sh

parent_path=$( cd "$(dirname "$0")" ; pwd -P )

cd "$parent_path"

productbuild --component MLAatKST.app /Applications -s $CERT_PKG MLAatKST-macOS-universal-v$1.pkg
