import mutagen

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
        self.attributeList = ["title", "artist", "album", "albumartist", "data",
                           "tracknumber", "tracktotal"]

    def setTitle(self,songTitle):
        self.title = songTitle

    def setArtist(self, artistName):
        self.artist = artistName

    def setAlbum(self,albumName):
        self.album = albumName

    def setAlbumArtist(self,albumArtistName):
        self.albumArtist = albumArtistName

    def setDate(self, songDate):
        self.date = songDate

    def setTrackNumber(self, songTrackNumber):
        self.trackNumber = songTrackNumber

    def setTrackTotal(self, songTrackTotal):
        self.trackTotal = songTrackTotal

    def setFileLocation(self, songFileLocation):
        self.fileLocation = songFileLocation

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

    def getSongInfoFromFile(self):
        """Reads file's metadata and stores it in the song object's data members"""

        # without the `[0]`, artist is a list of a string

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