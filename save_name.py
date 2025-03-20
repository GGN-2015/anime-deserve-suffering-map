import os
import functools

@functools.cache
def get_text():
    content = open("now-known.txt", "r", encoding="utf-8").read()
    return [line.split("\t") for line in content.split("\n")]

def get_text_by_sd(s, d):
    row_id = None
    for lid in range(21):
        if get_text()[lid][0] == str(s):
            row_id = lid
            break
    assert row_id is not None
    col_id = None
    for cid in range(21):
        if get_text()[0][cid] == str(d):
            col_id = cid
            break
    assert col_id is not None
    try:
        return get_text()[row_id][col_id].strip()
    except:
        return ""

if __name__ == "__main__":
    cnt = 0
    for s in range(5, 101, 5):
        for d in range(5, 101, 5):
            name_file = os.path.join("images", "s%03dd%03d" % (s, d), "name-anime.txt")
            if (name_anime := get_text_by_sd(s, d)) != "":
                cnt += 1
                with open(name_file, "w", encoding="utf-8") as fp:
                    fp.write(name_anime)
            else:
                if os.path.isfile(name_file):
                    os.remove(name_file)
    print("total known: %d" % cnt)