#!/bin/sh

parent_path=$( cd "$(dirname "$0")" ; pwd -P )

cd "$parent_path"

xgettext -C -k_ --from-code=utf-8 \
         -o ./de/LC_MESSAGES/mlaatkst.po \
         --join-existing \
         ../../src/*

msgfmt -o ./de/LC_MESSAGES/mlaatkst.mo ./de/LC_MESSAGES/mlaatkst.po
