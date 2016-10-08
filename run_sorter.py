import sortMusicFiles as SortMusicFiles
##############################################################
# below is code to test basic things

s = SortMusicFiles()
# for thing in os.walk("/mnt/c/Users/Ben/Music/Test OGG Music/Music/"):
#     print(thing)

s.setMusicFilesLocation("/mnt/a/Music/OGG Music")
s.setOutputFilesLocation("/mnt/a/Music/OGG Music testing")

# s.setMusicFilesLocation("/mnt/a/Music/sample music for testing")
# s.setOutputFilesLocation("/mnt/a/Music/testing")

# s.setMusicFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing")
# s.setOutputFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing_output")

s.sortFiles()

# s.Songs = ["hi"]
# s.resetObjectToDefault()