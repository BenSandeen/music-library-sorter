#### To be run using pytest testing library ####

import sortMusicFiles as SM
import song as Song
import sys

class TestClass:
    """pytest automatically finds and runs these tests.  The class is effectively a means
       of organizing the tests in logical compartments"""

    # def setup(self):
    #     self.song = Song.Song()

    def test_one(self):
        """Tests initialization of the song object"""
        self.song = Song.Song()
        assert self.song.getTitle() == "No title info"
        assert self.song.getArtist() == "No artist info"
        assert self.song.getAlbum() == "No album info"
        assert self.song.getAlbumArtist() == "No albumartist info"
        assert self.song.getDate() == "No date info"
        assert self.song.getTrackNumber() == "No tracknumber info"
        assert self.song.getTrackTotal() == "No tracktotal info"

    musicSorter = SM.SortMusicFiles()

    def test_two(self):
        """Tests intitialization of SortMusicFiles object"""
        assert self.musicSorter.musicFilesLocation  == ""
        assert self.musicSorter.outputFilesLocation == ""
        assert self.musicSorter.Songs               == []
        self.musicSorter.resetObjectToDefault()

    def test_three(self):
        """Tests getting user input"""
        self.musicSorter.resetObjectToDefault()

    def test_four(self):
        pass

    def test_five(self):
        pass

    def test_six(self):
        pass

    def test_seven(self):
        pass

    def test_eight(self):
        pass

    def test_nine(self):
        pass
