import sys
import re
import os

def get_name(s:int, d:int) -> str:
    dirnow  = os.path.dirname(os.path.abspath(__file__))
    aimpath = os.path.join(dirnow, "images", "s%03dd%03d" % (s, d), "name-anime.txt")

    if os.path.isfile(aimpath):
        return open(aimpath).read().strip()
    else:
        return "<unknown>"

if __name__ == "__main__":
    tag = sys.argv[1]
    assert re.match(r"s\d+d\d+", tag) or re.match(r"d\d+s\d+", tag)

    if re.match(r"s\d+d\d+", tag):
        lid, rid = tag.split("d")
    else:
        rid, lid = tag.split("s")

    lid = int(lid[1:])
    rid = int(rid)
    print("s%dd%d:" % (lid, rid), get_name(lid, rid))