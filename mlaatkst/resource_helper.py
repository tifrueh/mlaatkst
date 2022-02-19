# Copyright (C) 2021  Timo Früh
# full copyright notice in __main__.py


import os


class ResourceHelper:

    pkgdir = os.path.dirname(os.path.abspath(__file__))
    rcdir = os.path.join(pkgdir, "..", "resources")
    resources = os.listdir(rcdir)

    @classmethod
    def list_resources(cls):
        for rc in cls.resources:
            print(rc)

    @classmethod
    def get_resource_path(cls, name):
        resource = None

        for rc in cls.resources:
            if rc == name:
                resource = rc

        if resource:
            return os.path.join(cls.rcdir, resource)
        else:
            raise Exception(f"ERROR: Resource {name} not found ...")

    @classmethod
    def read_text_resource(cls, name):
        rc_path = cls.get_resource_path(name)

        with open(rc_path, "r") as rc:
            return rc.read()

    @classmethod
    def write_text_resource(cls, name, write):
        rc_path = cls.get_resource_path(name)

        with open(rc_path, "w") as rc:
            rc.write(write)