#### To be run using pytest testing library ####

import sortMusicFiles as SM
import song as Song
import sys

class TestClass:
    """pytest automatically finds and runs these tests.  The class is effectively a means
       of organizing the tests in logical compartments"""

    def setup(self):
        self.song = Song.Song()

    def test_one(self):
        assert self.song.getTitle() == "No title info"
        assert self.song.getArtist() == "No artist info"
        assert self.song.getAlbum() == "No album info"
        assert self.song.getAlbumArtist() == "No albumartist info"
        assert self.song.getDate() == "No date info"
        assert self.song.getTrackNumber() == "No tracknumber info"
        assert self.song.getTrackTotal() == "No tracktotal info"

    def setup(self):
        """TODO: may need to use mocking or something to create an object.
           Alternatively, you may just need to not initialize the self.musicLocation
           variable when creating a SortMusicFiles object"""
        sys.stdin.write("C://")
        self.musicSorter = SM.SortMusicFiles()
        sys.stdin.write("C://")

    def test_two(self):
        pass

    def test_three(self):
        pass

    def test_four(self):
        pass

    def test_five(self):
        pass

    def test_six(self):
        pass

    def test_seven(self):
        pass

    def test_eight(self):
        self.song.setArtist("Queen")
        assert 'Queen' in self.song.getArtist()

    # def test_nine(self):
