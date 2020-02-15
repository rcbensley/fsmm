#!/usr/bin/env python3

import os
import sys
import urllib.request
import shutil
from requests import get

def ez_download(d, r, u, f):
    h = {'Referer': r}
    d = os.path.join(d, f)
    if os.path.isfile(d):
        print("Skipping already existing file: {}".format(d))
        return
    else:
        print("Downloading {} to {}".format(u, d))
        with open(d, "wb") as download:
            r = get(u, headers=h)
            download.write(r.content)

if __name__ == "__main__":
    arg_count = len(sys.argv)

    mods_dir = os.path.join(os.environ['USERPROFILE'],
            "Documents\\My Games\\FarmingSimulator2019\\mods")

    if arg_count <= 1:
        sys.exit("Missing mods file")
    elif arg_count == 2:
        mods_file = str(sys.argv[1])
        if not os.path.isfile(mods_file):
            sys.exit("Failed to open file {}".format(mods_file))

    urls = list()
    with open(mods_file, 'r') as f:
        p = None
        for line in f:
            if line.endswith(".zip\n") or line.endswith(".zip"):
                urls.append([p.strip(), line.strip(), os.path.basename(line).strip()])
            else:
                p = line

    for download in urls:
        ez_download(mods_dir, *download)

