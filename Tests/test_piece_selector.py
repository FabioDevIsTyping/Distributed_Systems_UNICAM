import unittest
from BitTorrent.piece_selector import PieceSelector
from BitTorrent.torrent import Torrent
from BitTorrent.peer import Peer

class TestPieceSelector(unittest.TestCase):
    def setUp(self):
        self.torrent = Torrent(total_pieces=10)
        self.peer1 = Peer('peer1')
        self.peer2 = Peer('peer2')
        self.peer3 = Peer('peer3')
        self.torrent.add_peer(self.peer1)
        self.torrent.add_peer(self.peer2)
        self.torrent.add_peer(self.peer3)
        self.piece_selector = PieceSelector(self.torrent)

    def test_random_first(self):
        self.peer2.add_piece(1)
        self.peer3.add_piece(2)
        self.peer3.add_piece(3)

        piece = self.piece_selector.random_first(self.peer1)
        self.assertIn(piece, range(10))
        self.assertFalse(self.peer1.has_piece(piece))

    def test_random_first_no_pieces_left(self):
        for i in range(self.torrent.total_pieces):
            self.peer1.add_piece(i)

        piece = self.piece_selector.random_first(self.peer1)
        self.assertIsNone(piece)

    def test_rarest_first(self):
        self.peer2.add_piece(0)
        self.peer3.add_piece(0)
        self.peer3.add_piece(1)

        piece = self.piece_selector.rarest_first(self.peer1)
        self.assertIsNotNone(piece)
        self.assertFalse(self.peer1.has_piece(piece))
        self.assertEqual(piece, 2)  # Updated to reflect correct expectation

    def test_rarest_first_no_pieces_left(self):
        for i in range(self.torrent.total_pieces):
            self.peer1.add_piece(i)

        piece = self.piece_selector.rarest_first(self.peer1)
        self.assertIsNone(piece)

    def test_rarest_first_all_pieces_same_rarity(self):
        for i in range(5):
            self.peer2.add_piece(i)
            self.peer3.add_piece(i)

        piece = self.piece_selector.rarest_first(self.peer1)
        self.assertIsNotNone(piece)
        self.assertFalse(self.peer1.has_piece(piece))

    def test_rarest_first_some_pieces_not_in_peers(self):
        self.peer2.add_piece(1)
        self.peer3.add_piece(1)
        self.peer3.add_piece(2)

        piece = self.piece_selector.rarest_first(self.peer1)
        self.assertIsNotNone(piece)
        self.assertFalse(self.peer1.has_piece(piece))
        self.assertEqual(piece, 0)  # Assuming pieces not in peers are considered rarest

if __name__ == '__main__':
    unittest.main()
