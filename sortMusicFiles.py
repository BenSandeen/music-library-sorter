import unicodedata as ud
import song as Song
import os
import mutagen

class SortMusicFiles:
    def __init__(self):
        self.musicFilesLocation = ""
        self.outputFilesLocation = ""
        self.Songs = []

    def resetObjectToDefault(self):
        """Used only for testing, so we don't have to create a bunch of separate objects"""
        self.__init__()

    def setMusicFilesLocation(self, fileLoc):
        self.musicFilesLocation = fileLoc

    def setMusicFilesLocationFromUserInput(self):
        """This may be updated in the future with a GUI"""
        self.setMusicFilesLocation(self.removeBadSymbolsInPathName(raw_input("What is the path where your music is located?\t")))

    def getMusicFilesLocation(self):
        return self.musicFilesLocation

    def setOutputFilesLocation(self, fileLoc):
        self.outputFilesLocation = fileLoc

    def setOutputFilesLocationFromUserInput(self):
        """This may be updated in the future with a GUI"""
        self.setOutputFilesLocation(
            self.removeBadSymbolsInPathName(raw_input("What is the path where you wish to put your music?\t")))

    def getOutputFilesLocation(self):
        return self.outputFilesLocation

    def findSongs(self):
        """Searches musicFilesLocation for music files, then puts it in Songs list

        TODO: We will want to make it so that the program can recursively search a
        directory at some point, but not now"""
        if self.musicFilesLocation == "":
            raise IOError

        musicFileExtensions = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.amr',
                               '.ape', '.au', '.awb', '.dct', '.dss', '.dvf', '.flac',
                               '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf',
                               '.mp3', '.mpc', '.msv', '.ogg', '.oga', '.mogg', '.opus',
                               '.ra', '.rm', '.raw', '.sln', '.tta', '.vox', '.wav',
                               '.wma', '.wv', '.webm']
        # dirQueue = [] # queue for holding directories, so we can recurse into them
        for thing in os.listdir(self.musicFilesLocation):
            for ext in musicFileExtensions:
                if ext in thing:
                    # this will need to append a song object in the future
                    self.Songs.append(thing)

    def removeBadSymbolsInPathName(self, path):
        """Removes symbols incompatible Windows's file system"""
        prohibitedSymbolsInWindowsPaths = ["\\", "/", ":", "\"", "*", "?", "<", ">", "|"]
        substituteSymbolsInWindowsPaths = ["--", "--", ";", "'", "_", "_", "(", ")", "_"]
        if type(path) == type(u'unicodeStr'):
            path = ud.normalize("NFKD", path).encode("ascii", "ignore")
        # nameStr = repr(nameStr)
        for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
            if badSymbol in path:
                path = str(path).replace(badSymbol, substituteSymbolsInWindowsPaths[idx])
        return path

    # def getSongInfoAndCreateSongObject(self):

##############################################################
# below is code to test basic things

# s = SortMusicFiles()
# s.setMusicFilesLocation("poop")
# s.setOutputFilesLocation("output")
# s.Songs = ["hi"]
# s.resetObjectToDefault()
