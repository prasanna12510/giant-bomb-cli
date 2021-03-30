import unittest

from giantbomb_cli import search_games
from giantbomb_cli import display_game_dlc
import config


class TestGiantBombCLI(unittest.TestCase):
    def test_search_games(self):
        """
        Test that it returns 200 status response
        """
        config.search='ape'
        status_code = search_games(config.search)
        self.assertEqual(status_code, 200)

    def test_display_game_dlc(self):
        """
        Test that it returns 200 status response
        """
        config.showdlc = True
        config.gid= '609'
        status_code = display_game_dlc(config.gid)
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
