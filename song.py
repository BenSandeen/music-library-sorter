import mutagen, os , unicodedata as ud
# import unidecode as ud

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

    def cleanStrings(self, string):
        """Converts unicode to ASCII and removes symbols incompatible with
        Windows's file system"""
        prohibitedSymbolsInWindowsPaths = ["\\", "/", ":", "\"", "*", "?", "<", ">", "|"]
        substituteSymbolsInWindowsPaths = ["--", "--", ";", "'", "_", "_", "(", ")", "_"]
        if type(string) == 'unicode': #type(u'unicodeStr'):
            try:
                string = ud.normalize("NFKC", string)
                # string = string.decode("utf-8")
                string = string.encode("ascii", "ignore")
            except Exception as e:
                print ("String on which error was encountered:\t",string)
                print(e)
        # nameStr = repr(nameStr)
        for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
            if badSymbol in string:
                try:
                    string = str(string).replace(badSymbol, substituteSymbolsInWindowsPaths[idx])
                except Exception as e:
                    print(e)
                    print("String on which error was encountered:\t",string)
        return string

    def setTitle(self, songTitle):
        try:
            songTitle = self.cleanStrings(songTitle)
            # print("SONGTITLE:\t",songTitle)
            self.title = songTitle
        except IOError as e: # maybe we were passed a file object???
            print(e)

    def setArtist(self, artistName):
        try:
            artistName = self.cleanStrings(artistName)
            self.artist = artistName
        except IOError as e:
            print(e)

    def setAlbum(self, albumName):
        try:
            albumName = self.cleanStrings(albumName)
            self.album = albumName
        except IOError as e:
            print(e)

    def setAlbumArtist(self, albumArtistName):
        try:
            albumArtistName = self.cleanStrings(albumArtistName)
            self.albumArtist = albumArtistName
        except IOError as e:
            print(e)

    def setDate(self, songDate):
        try:
            songDate = self.cleanStrings(songDate)
            self.date = songDate
        except IOError as e:
            print(e)

    def setTrackNumber(self, songTrackNumber):
        try:
            songTrackNumber = self.cleanStrings(songTrackNumber)
            self.trackNumber = songTrackNumber
        except IOError as e:
            print(e)

    def setTrackTotal(self, songTrackTotal):
        try:
            songTrackTotal = self.cleanStrings(songTrackTotal)
            self.trackTotal = songTrackTotal
        except IOError as e:
            print(e)

    def setFileLocation(self, songFileLocation):
        try:
            # songFileLocation = self.cleanStrings(songFileLocation)
            self.fileLocation = songFileLocation
        except IOError as e:
            print(e)

    def setFileName(self, songFileName):
        try:
            songFileName = self.cleanStrings(songFileName)
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

        # print(mutagen.File(self.fileLocation))
        try:
            self.setTitle(((mutagen.File(self.fileLocation + self.fileName))["title"])[0])
        except: pass

        try:
            self.setArtist(((mutagen.File(self.fileLocation + self.fileName))["artist"])[0])
        except: pass

        try:
            # print("file location:\t",self.fileLocation + self.fileName)
            self.setAlbum(((mutagen.File(self.fileLocation + self.fileName))["album"])[0])
        except: print ("couldn't find album")#pass

        try:
            self.setAlbumArtist(((mutagen.File(self.fileLocation + self.fileName))["albumartist"])[0])
        except: pass

        try:
            self.setDate(((mutagen.File(self.fileLocation + self.fileName))["artist"])[0])
        except: pass

        try:
            self.setTrackNumber(((mutagen.File(self.fileLocation + self.fileName))["tracknumber"])[0])
        except: pass

        try:
            self.setTrackTotal(((mutagen.File(self.fileLocation + self.fileName))["tracktotal"])[0])
        except: pass

        dataMemberList = []
        # for attribute in self.attributeList:
        #     try:
        #         mutagen.File


# s = Song()
# s.setFileLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing/[Mix] One and a half hours of future bass, nu funk, electro, ect.ogg")
# s.getSongInfoFromFile()