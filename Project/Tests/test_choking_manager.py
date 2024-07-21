import unittest
from BitTorrent.peer import Peer
from BitTorrent.torrent import Torrent
from BitTorrent.choking_manager import ChokingManager

class TestChokingManager(unittest.TestCase):
    def setUp(self):
        """
        Set up a Torrent instance, several Peer instances, and a ChokingManager for testing.
        """
        self.torrent = Torrent(total_pieces=100)
        self.peer1 = Peer('peer1')
        self.peer2 = Peer('peer2')
        self.peer3 = Peer('peer3')
        self.peer4 = Peer('peer4')
        self.peer5 = Peer('peer5')

        self.torrent.add_peer(self.peer1)
        self.torrent.add_peer(self.peer2)
        self.torrent.add_peer(self.peer3)
        self.torrent.add_peer(self.peer4)
        self.torrent.add_peer(self.peer5)

        self.choking_manager = ChokingManager(self.torrent, unchoke_slots=3, optimistic_unchoke_interval=2)

    def test_initial_state(self):
        """
        Test the initial state of the ChokingManager.
        """
        self.assertIsNone(self.choking_manager.optimistically_unchoked_peer)
        self.assertEqual(self.choking_manager.optimistic_unchoke_counter, 0)

    def test_manage_choking(self):
        """
        Test the manage_choking method.
        """
        self.choking_manager.manage_choking()
        unchoked_peers = [peer for peer in self.torrent.peers if not peer.is_choked]
        choked_peers = [peer for peer in self.torrent.peers if peer.is_choked]

        self.assertEqual(len(unchoked_peers), 3)
        self.assertEqual(len(choked_peers), 2)
        print(f"Unchoked peers: {[peer.peer_id for peer in unchoked_peers]}")
        print(f"Choked peers: {[peer.peer_id for peer in choked_peers]}")

    def test_optimistic_unchoking(self):
        """
        Test the optimistic unchoking mechanism.
        """
        # Run manage_choking enough times to trigger optimistic unchoking
        self.choking_manager.manage_choking()
        self.choking_manager.manage_choking()

        # Check that one additional peer is unchoked optimistically
        unchoked_peers = [peer for peer in self.torrent.peers if not peer.is_choked]
        choked_peers = [peer for peer in self.torrent.peers if peer.is_choked]

        self.assertEqual(len(unchoked_peers), 4)
        self.assertEqual(len(choked_peers), 1)
        self.assertIsNotNone(self.choking_manager.optimistically_unchoked_peer)
        self.assertIn(self.choking_manager.optimistically_unchoked_peer, unchoked_peers)
        print(f"Unchoked peers after optimistic unchoking: {[peer.peer_id for peer in unchoked_peers]}")

    def test_unchoke_and_rechoke(self):
        """
        Test that the optimistically unchoked peer is rechoked correctly.
        """
        # Run manage_choking enough times to trigger optimistic unchoking
        self.choking_manager.manage_choking()
        self.choking_manager.manage_choking()

        first_optimistically_unchoked_peer = self.choking_manager.optimistically_unchoked_peer

        # Run manage_choking again to possibly rechoke the previous optimistic peer
        self.choking_manager.manage_choking()

        if first_optimistically_unchoked_peer:
            self.assertTrue(first_optimistically_unchoked_peer.is_choked or
                            self.choking_manager.optimistically_unchoked_peer == first_optimistically_unchoked_peer)

if __name__ == '__main__':
    unittest.main()
