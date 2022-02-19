# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py


import pathlib


class ResourceHelper:

    pkgdir = pathlib.PurePath(__file__).parent
    rcdir = pkgdir.parent.joinpath("resources")

    print(rcdir)

    @classmethod
    def get_resource_path(cls, name):
        rc_path = pathlib.Path(cls.rcdir.joinpath(name))
        if rc_path.exists():
            return rc_path
        else:
            raise Exception(f"ERROR: Resource {name} not found ...")

    @classmethod
    def read_text_resource(cls, name):
        rc_path = cls.get_resource_path(name)

        return rc_path.read_text()

    @classmethod
    def write_text_resource(cls, name, write):
        rc_path = cls.get_resource_path(name)

        rc_path.write_text(write)
