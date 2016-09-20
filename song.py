import mutagen, os

class Song:
    def __init__(self):
        self.title = "No title info"
        self.artist = "No artist info"
        self.album = "No album info"
        self.albumArtist = "No albumartist info"
        self.date = "No date info"
        self.trackNumber = "No tracknumber info"
        self.trackTotal = "No tracktotal info"
        self.fileLocation = "No file location info"
        self.fileName = "No file name info"
        self.attributeList = ["title", "artist", "album", "albumartist", "data",
                           "tracknumber", "tracktotal"]

    # we don't perform any checks on the data because we're
    def setTitle(self, songTitle):
        try:
            songTitle = str(songTitle)
            self.title = songTitle
        except IOError as e: # maybe we were passed a file object???
            print(e)

    def setArtist(self, artistName):
        try:
            artistName = str(artistName)
            self.artist = artistName
        except IOError as e:
            print(e)

    def setAlbum(self, albumName):
        try:
            albumName = str(albumName)
            self.album = albumName
        except IOError as e:
            print(e)

    def setAlbumArtist(self, albumArtistName):
        try:
            albumArtistName = str(albumArtistName)
            self.albumArtist = albumArtistName
        except IOError as e:
            print(e)

    def setDate(self, songDate):
        try:
            songDate = str(songDate)
            self.date = songDate
        except IOError as e:
            print(e)

    def setTrackNumber(self, songTrackNumber):
        try:
            songTrackNumber = str(songTrackNumber)
            self.trackNumber = songTrackNumber
        except IOError as e:
            print(e)

    def setTrackTotal(self, songTrackTotal):
        try:
            songTrackTotal = str(songTrackTotal)
            self.trackTotal = songTrackTotal
        except IOError as e:
            print(e)

    def setFileLocation(self, songFileLocation):
        try:
            songFileLocation = str(songFileLocation)
            self.fileLocation = songFileLocation
        except IOError as e:
            print(e)

    def setFileName(self, songFileName):
        try:
            songFileName = str(songFileName)
            self.fileName = songFileName
        except IOError as e:
            print(e)

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def getAlbum(self):
        return self.album

    def getAlbumArtist(self):
        return self.albumArtist

    def getDate(self):
        return self.date

    def getTrackNumber(self):
        return self.trackNumber

    def getTrackTotal(self):
        return self.trackTotal

    def getFileLocation(self):
        return self.fileLocation

    def getFileName(self):
        return self.fileName

    def getSongInfoFromFile(self):
        """Reads file's metadata and stores it in the song object's data members"""

        # without the `[0]`, artist is a list of a string
        # self.setFileLocation(os.getcwd())

        print(mutagen.File(self.fileLocation))
        try:
            self.setTitle(((mutagen.File(self.fileLocation))["title"])[0])
        except: pass

        try:
            self.setArtist(((mutagen.File(self.fileLocation))["artist"])[0])
        except: pass

        try:
            self.setAlbum(((mutagen.File(self.fileLocation))["album"])[0])
        except: pass

        try:
            self.setAlbumArtist(((mutagen.File(self.fileLocation))["albumartist"])[0])
        except: pass

        try:
            self.setDate(((mutagen.File(self.fileLocation))["artist"])[0])
        except: pass

        try:
            self.setTrackNumber(((mutagen.File(self.fileLocation))["tracknumber"])[0])
        except: pass

        try:
            self.setTrackTotal(((mutagen.File(self.fileLocation))["tracktotal"])[0])
        except: pass

        dataMemberList = []
        # for attribute in self.attributeList:
        #     try:
        #         mutagen.File


s = Song()
s.setFileLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing/[Mix] One and a half hours of future bass, nu funk, electro, ect.ogg")
s.getSongInfoFromFile()