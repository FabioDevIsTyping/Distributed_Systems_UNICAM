from BitTorrent.peer import Peer

class Torrent:
    def __init__(self, total_pieces):
        """
        Initializes a new Torrent object.

        :param total_pieces: Total number of pieces in the torrent.
        """
        self.total_pieces = total_pieces
        self.peers = []

    def add_peer(self, peer):
        """
        Adds a peer to the torrent.

        :param peer: The Peer object to add.
        """
        if not any(p.peer_id == peer.peer_id for p in self.peers):
            self.peers.append(peer)
            print(f"Peer {peer.peer_id} added to the torrent.")
        else:
            print(f"Peer {peer.peer_id} already exists in the torrent.")

    def remove_peer(self, peer_id):
        """
        Removes a peer from the torrent.

        :param peer_id: The ID of the peer to remove.
        """
        self.peers = [peer for peer in self.peers if peer.peer_id != peer_id]
        print(f"Peer {peer_id} removed from the torrent.")

    def get_peers_with_piece(self, piece_index):
        """
        Gets the list of peers that have a specific piece.

        :param piece_index: The index of the piece.
        :return: List of peers that have the piece.
        """
        return [peer for peer in self.peers if peer.has_piece(piece_index)]

    def broadcast_piece(self, peer_id, piece_index):
        """
        Broadcasts that a peer has received a piece to all other peers.

        :param peer_id: The ID of the peer that received the piece.
        :param piece_index: The index of the piece.
        """
        for peer in self.peers:
            if peer.peer_id != peer_id:
                peer.add_piece(piece_index)
        print(f"Peer {peer_id} broadcasted piece {piece_index} to all peers.")

    def __str__(self):
        """
        Returns a string representation of the torrent.
        """
        return f"Torrent(Total pieces: {self.total_pieces}, Peers: {[peer.peer_id for peer in self.peers]})"