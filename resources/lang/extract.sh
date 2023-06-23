#!/bin/sh

parent_path=$( cd "$(dirname "$0")" ; pwd -P )

cd "$parent_path"

xgettext -C -k_ --from-code=utf-8 \
         -o ./de/LC_MESSAGES/messages.po \
         --copyright-holder='Timo Früh' \
         --package-name='MLAatKST' \
         --msgid-bugs-address='timo.frueh@icloud.com' \
         --join-existing \
         ../../src/*

msgfmt -o ./de/LC_MESSAGES/messages.mo ./de/LC_MESSAGES/messages.po
