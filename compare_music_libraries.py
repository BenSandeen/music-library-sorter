import os

print(os.getcwd())
# desktop_music_lib = "/mnt/a/Music/OGG Music"
# ext_hdd_lib = "/mnt/f/OGG Music"
desktop_music_lib = "A:\Music\OGG Music"
ext_hdd_lib = "F:\OGG Music"
work_ext_hdd_lib = "/media/ben/Sparta Take Two/OGG Music"
work_music_lib = "/mnt/Windows/Users/BenjaminSandeen/Music/OGG Music"

#### BELOW IS FOR WINDOWS!!! ####

def compare_libs_on_windows():
    # ext_hdd_dir = os.listdir(ext_hdd_lib)
    work_ext_hdd_dir = os.listdir(work_ext_hdd_lib)

    # for artist in os.listdir(desktop_music_lib):
    for artist in os.listdir(work_music_lib):
        # if artist not in ext_hdd_dir:
        if artist not in work_ext_hdd_lib:
            print(artist)

    print("BREAK")

    # desktop_music_dir = os.listdir(desktop_music_lib)
    work_music_dir = os.listdir(work_music_lib)
    # for artist in desktop_music_dir:
    for artist in work_music_dir:
        # for album in os.listdir(desktop_music_lib + "\\" + artist):
        for album in os.listdir(work_music_lib + "\\" + artist):
            # print(album)
            # for ext_hdd_album in ext_hdd_dir[ext_hdd_dir.index(artist)]:
            # print(ext_hdd_lib + "\\" + artist)
            try:
                # for ext_hdd_album in os.listdir(ext_hdd_lib + "\\" + artist):
                    # if ext_hdd_album == album:
                    #     print("match")
                # if album not in os.listdir(ext_hdd_lib + "\\" + artist):
                if album not in os.listdir(work_ext_hdd_lib + "\\" + artist):
                    print("Artist:\t", artist, "\tAlbum:\t", album)
            except FileNotFoundError:
                print("Missing artist:\t", artist)


#### BELOW IS FOR LINUX!!! ####

work_ext_hdd_dir = os.listdir(work_ext_hdd_lib)

def compare_libs_on_linux():
    for artist in os.listdir(work_ext_hdd_lib):
        if artist not in work_music_lib:
            print(artist)

    print("BREAK")

    work_music_dir = os.listdir(work_music_lib)
    for artist in work_ext_hdd_dir:
        for album in os.listdir(work_ext_hdd_lib + "/" + artist):
            try:
                if album not in os.listdir(work_music_lib + "/" + artist):
                    print("Artist:\t", artist, "\tAlbum:\t", album)
            except FileNotFoundError:
                print("Missing artist:\t", artist)


linux_or_windows = input("Are you using Windows or Linux?")
if linux_or_windows.lower() == "windows":
    compare_libs_on_windows()
elif linux_or_windows.lower() == "linux":
    compare_libs_on_linux()
else:
    print("BAD INPUT!!")
