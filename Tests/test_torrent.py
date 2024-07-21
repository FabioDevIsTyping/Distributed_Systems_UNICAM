# tests/test_torrent.py

import unittest
from BitTorrent.peer import Peer
from BitTorrent.torrent import Torrent

class TestTorrent(unittest.TestCase):
    def setUp(self):
        """
        Set up a Torrent instance and some Peer instances for testing.
        """
        self.torrent = Torrent(total_pieces=100)
        self.peer1 = Peer('peer1')
        self.peer2 = Peer('peer2')
        self.peer3 = Peer('peer3')

    def test_add_peer(self):
        """
        Test adding peers to the torrent.
        """
        # Add peer1 to the torrent
        self.torrent.add_peer(self.peer1)
        # Check that peer1 is added
        self.assertIn(self.peer1, self.torrent.peers)
        # Try adding peer1 again and ensure it's not added twice
        self.torrent.add_peer(self.peer1)
        self.assertEqual(len(self.torrent.peers), 1)

    def test_remove_peer(self):
        """
        Test removing peers from the torrent.
        """
        # Add peers to the torrent
        self.torrent.add_peer(self.peer1)
        self.torrent.add_peer(self.peer2)
        # Remove peer1 from the torrent
        self.torrent.remove_peer(self.peer1.peer_id)
        # Check that peer1 is removed
        self.assertNotIn(self.peer1, self.torrent.peers)
        # Check that peer2 is still in the torrent
        self.assertIn(self.peer2, self.torrent.peers)

    def test_get_peers_with_piece(self):
        """
        Test getting the list of peers that have a specific piece.
        """
        # Add peers and pieces to the torrent
        self.peer1.add_piece(1)
        self.peer2.add_piece(2)
        self.peer3.add_piece(1)
        self.torrent.add_peer(self.peer1)
        self.torrent.add_peer(self.peer2)
        self.torrent.add_peer(self.peer3)
        # Get peers with piece 1
        peers_with_piece_1 = self.torrent.get_peers_with_piece(1)
        # Check that peers with piece 1 are peer1 and peer3
        self.assertIn(self.peer1, peers_with_piece_1)
        self.assertIn(self.peer3, peers_with_piece_1)
        # Check that peer2 is not in the list of peers with piece 1
        self.assertNotIn(self.peer2, peers_with_piece_1)

    def test_broadcast_piece(self):
        """
        Test broadcasting a piece to all peers.
        """
        # Add peers to the torrent
        self.torrent.add_peer(self.peer1)
        self.torrent.add_peer(self.peer2)
        self.torrent.add_peer(self.peer3)
        # Broadcast piece 3 from peer1
        self.torrent.broadcast_piece(self.peer1.peer_id, 3)
        # Check that all peers except peer1 received piece 3
        self.assertIn(3, self.peer2.pieces)
        self.assertIn(3, self.peer3.pieces)
        self.assertNotIn(3, self.peer1.pieces)  # peer1 should not receive its own broadcast

    def test_str_representation(self):
        """
        Test the string representation of the torrent.
        """
        # Add peers to the torrent
        self.torrent.add_peer(self.peer1)
        self.torrent.add_peer(self.peer2)
        # Get the string representation of the torrent
        torrent_str = str(self.torrent)
        # Check that the string correctly represents the torrent's state
        expected_str = "Torrent(Total pieces: 100, Peers: ['peer1', 'peer2'])"
        self.assertEqual(torrent_str, expected_str)

if __name__ == '__main__':
    unittest.main()
