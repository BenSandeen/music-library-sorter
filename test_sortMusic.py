#### To be run using pytest testing library ####

import sortMusic as SM

class TestClass:
    """pytest automatically finds and runs these tests.  The class is effectively a means
       of organizing the tests in logical compartments"""

    def setup(self):
        self.song = SM.Song()

    def test_one(self):
        assert self.song.getTitle() == "No title info"

    def test_two(self):
        assert self.song.getArtist() == "No artist info"

    def test_three(self):
        assert self.song.getAlbum() == "No album info"

    def test_five(self):
        assert self.song.getAlbumArtist() == "No albumartist info"

    def test_six(self):
        assert self.song.getDate() == "No date info"

    def test_seven(self):
        assert self.song.getTrackNumber() == "No tracknumber info"

    def test_eight(self):
        assert self.song.getTrackTotal() == "No tracktotal info"

    def test_seven(self):
        self.song.setArtist("Queen")
        assert 'Queen' in self.song.getArtist()

    # def test_three(self):
