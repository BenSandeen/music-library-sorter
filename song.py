class Song:
    def __init__(self):
        self.title = "No title info"
        self.artist = "No artist info"
        self.album = "No album info"
        self.albumArtist = "No albumartist info"
        self.date = "No date info"
        self.trackNumber = "No tracknumber info"
        self.trackTotal = "No tracktotal info"

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
