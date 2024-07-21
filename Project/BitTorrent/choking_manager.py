import random
from BitTorrent.peer import Peer
from BitTorrent.torrent import Torrent


class ChokingManager:
    def __init__(self, torrent, unchoke_slots=4, optimistic_unchoke_interval=3):
        """
        Initializes the ChokingManager.

        :param torrent: The Torrent object managing the peers.
        :param unchoke_slots: Number of peers to unchoke at a time.
        :param optimistic_unchoke_interval: Interval for optimistic unchoking.
        """
        self.torrent = torrent
        self.unchoke_slots = unchoke_slots
        self.optimistic_unchoke_interval = optimistic_unchoke_interval
        self.optimistically_unchoked_peer = None
        self.optimistic_unchoke_counter = 0

    def manage_choking(self):
        """
        Manages choking and unchoking of peers based on download rates and optimistic unchoking.
        """
        # Simulate download rates for peers
        peers = list(self.torrent.peers)
        download_rates = {peer: random.randint(1, 100) for peer in peers}

        # Sort peers by simulated download rate in descending order
        peers.sort(key=lambda peer: download_rates[peer], reverse=True)

        unchoked_peers = []
        for i, peer in enumerate(peers):
            if i < self.unchoke_slots:
                peer.unchoke()
                unchoked_peers.append(peer)
            else:
                peer.choke()

        print(f"Regularly unchoked peers: {[peer.peer_id for peer in unchoked_peers]}")

        # Optimistic Unchoking
        self.optimistic_unchoke_counter += 1
        if self.optimistic_unchoke_counter >= self.optimistic_unchoke_interval:
            self.optimistic_unchoke_counter = 0
            self.optimistically_unchoke(peers, unchoked_peers)

    def optimistically_unchoke(self, peers, unchoked_peers):
        """
        Optimistically unchokes a random choked peer.
        """
        choked_peers = [peer for peer in peers if peer.is_choked and peer not in unchoked_peers]
        if choked_peers:
            # If there is an already optimistically unchoked peer, choke it before unchoking a new one
            if self.optimistically_unchoked_peer and self.optimistically_unchoked_peer.is_choked is False:
                self.optimistically_unchoked_peer.choke()

            self.optimistically_unchoked_peer = random.choice(choked_peers)
            self.optimistically_unchoked_peer.unchoke()
            print(f"Optimistically unchoked peer: {self.optimistically_unchoked_peer.peer_id}")
        else:
            self.optimistically_unchoked_peer = None

        total_unchoked_peers = unchoked_peers + (
            [self.optimistically_unchoked_peer] if self.optimistically_unchoked_peer else [])
        print(f"Total unchoked peers after optimistic unchoking: {[peer.peer_id for peer in total_unchoked_peers]}")