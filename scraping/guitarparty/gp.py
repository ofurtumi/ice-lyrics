import urllib3
import json
import re


api = "https://www.guitarparty.com/api/v3/core/songs/"

def format_song(raw_song):
    song = re.sub(r"\[.*?\]", "", raw_song)
    song = re.sub(r"\{.*?\}", "", song)
    song = re.sub(r"\(.*?\)", "", song)
    song = re.sub(r" +", " ", song)
    song = [line.strip() for line in song.split("\n") if line.strip() != ""]
    return song

def get_song(id):
    page = urllib3.request("GET", api + id)
    data = page.json()
    song = format_song(data["song"])
    title = data["title"]
    return title, song

def get_ids():
    limit = 1859
    ids = []
    http = urllib3.PoolManager()
    for i in range(limit):
        url = api + f"?format=json&limit=10&offset={ i * 10 }"
        try:
            print(f"{i}/{limit - 1} - ids: {len(ids)}", end='\r')
            page = http.request("GET", url)
            data = page.json()
            new_ids = [song["id"] for song in data["results"] if song["language"] == "is"]
            if len(new_ids) != 0:
                ids = ids + new_ids

                # append to file
                with open("ids.txt", "a") as f:
                    f.write("\n")
                    f.write("\n".join(list(map(str, new_ids))))

        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            exit()
        except:
            print(f"Error: failed at offset {i}")

    return ids

def write_songs():
    with open("ids.txt", "r") as f:
        ids = f.read().split("\n")

    songs = dict()
    last_song = ""
    for i, id in enumerate( ids ):
        print(f"{i}/{len(ids) - 1} - songs: {len(songs):4} - {last_song}", end='\r')
        try:
            title, song = get_song(id)
            last_song = title
            songs[title] = song
        except Exception as e:
            if (e == "KeyboardInterrupt"):
                exit()
            print(e)
    return songs

# pínu hausverkur að keyra þetta
# fyrsta skref er að keyra get_ids() til að fá lista af öllum id, gæti tekið kringum 30-60 mín
# næst þarf að keyra write_songs() til að fá öll lög, gæti tekið 10-20 mín

# einfaldast bara að henda þessu fyrir neðan í gang og labba í burtu
# get_ids()
# with open("gp.json", "w") as f:
#     json.dump(write_songs(), f, ensure_ascii=False, indent=2)
