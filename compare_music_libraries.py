import os

print(os.getcwd())
# desktop_music_lib = "/mnt/a/Music/OGG Music"
# ext_hdd_lib = "/mnt/f/OGG Music"
desktop_music_lib = "A:\Music\OGG Music"
ext_hdd_lib = "F:\OGG Music"

ext_hdd_dir = os.listdir(ext_hdd_lib)

for artist in os.listdir(desktop_music_lib):
    if artist not in ext_hdd_dir:
        print(artist)

print("BREAK")

desktop_music_dir = os.listdir(desktop_music_lib)
for artist in desktop_music_dir:
    for album in os.listdir(desktop_music_lib + "\\" + artist):
        # print(album)
        # for ext_hdd_album in ext_hdd_dir[ext_hdd_dir.index(artist)]:
        # print(ext_hdd_lib + "\\" + artist)
        try:
            # for ext_hdd_album in os.listdir(ext_hdd_lib + "\\" + artist):
                # if ext_hdd_album == album:
                #     print("match")
            if album not in os.listdir(ext_hdd_lib + "\\" + artist):
                print("Artist:\t", artist, "\tAlbum:\t", album)
        except FileNotFoundError:
            print("Missing artist:\t", artist)
            # if album not in
    # break

