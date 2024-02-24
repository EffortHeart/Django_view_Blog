# common.utilitary.py

import hashlib
from datetime import datetime


def img_url(self, filename):
    hash_ = hashlib.md5()
    hash_.update(str(filename).encode("utf-8") + str(datetime.now()).encode("utf-8"))
    file_hash = hash_.hexdigest()

    if self.__class__.__name__ == "Category":
        filename = self.slug + "." + str(filename.split(".")[-1])
    else:
        filename = filename
    return "{0}{1}/{2}".format(self.file_prepend, file_hash, filename)
