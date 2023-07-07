#!/bin/sh

parent_path=$( cd "$(dirname "$0")" ; pwd -P )

cd "$parent_path"

if [ ! $1 ]; then
    echo "Usage: package.sh [VERSION NUMBER]"
    exit
fi

productbuild --component MLAatKST.app /Applications -s $CERT_PKG MLAatKST-macOS-universal-v$1.pkg
