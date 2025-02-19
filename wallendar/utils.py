import os


def can_create_file(filename):
    base_dir = os.path.dirname(filename)
    if not (
        not os.path.exists(filename)
        and os.path.isdir(base_dir)
        and os.access(base_dir, os.W_OK)
    ):
        raise IOError("Unable to write to target path")
