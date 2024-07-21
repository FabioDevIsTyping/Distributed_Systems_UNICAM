# tests/test_peer.py

import unittest
from BitTorrent.peer import Peer

class TestPeer(unittest.TestCase):
    def setUp(self):
        """
        Set up a peer instance for testing.
        """
        self.peer = Peer('peer1')

    def test_initial_state(self):
        """
        Test the initial state of a new peer.
        """
        # The peer should be choked initially
        self.assertTrue(self.peer.is_choked)
        # The peer should not be interested initially
        self.assertFalse(self.peer.is_interested)
        # The peer should have no pieces initially
        self.assertEqual(len(self.peer.pieces), 0)

    def test_add_piece(self):
        """
        Test adding a piece to the peer's collection.
        """
        # Add piece 1 to the peer
        self.peer.add_piece(1)
        # Check if piece 1 is in the peer's collection
        self.assertIn(1, self.peer.pieces)

    def test_has_piece(self):
        """
        Test checking if the peer has a specific piece.
        """
        # Add piece 2 to the peer
        self.peer.add_piece(2)
        # The peer should have piece 2
        self.assertTrue(self.peer.has_piece(2))
        # The peer should not have piece 1
        self.assertFalse(self.peer.has_piece(1))

    def test_choke_unchoke(self):
        """
        Test choking and unchoking the peer.
        """
        # Unchoke the peer
        self.peer.unchoke()
        # The peer should be unchoked
        self.assertFalse(self.peer.is_choked)
        # Choke the peer
        self.peer.choke()
        # The peer should be choked
        self.assertTrue(self.peer.is_choked)

    def test_express_withdraw_interest(self):
        """
        Test expressing and withdrawing interest.
        """
        # Express interest in downloading pieces
        self.peer.express_interest()
        # The peer should be interested
        self.assertTrue(self.peer.is_interested)
        # Withdraw interest in downloading pieces
        self.peer.withdraw_interest()
        # The peer should not be interested
        self.assertFalse(self.peer.is_interested)

    def test_str_representation(self):
        """
        Test the string representation of the peer.
        """
        # Add some pieces to the peer
        self.peer.add_piece(1)
        self.peer.add_piece(2)
        # Get the string representation of the peer
        peer_str = str(self.peer)
        # The string should correctly represent the peer's state
        expected_str = "Peer(peer1, Choked: True, Interested: False, Pieces: [1, 2])"
        self.assertEqual(peer_str, expected_str)

if __name__ == '__main__':
    unittest.main()
