import random
from collections import Counter


class PieceSelector:
    def __init__(self, torrent):
        """
        Initializes the PieceSelector with a given torrent.

        :param torrent: The Torrent object managing the peers and pieces.
        """
        self.torrent = torrent

    def random_first(self, peer):
        """
        Selects a random piece that the given peer doesn't have.

        :param peer: The peer for which to select a piece.
        :return: The index of the selected piece, or None if no pieces are available.
        """
        # Identify pieces that the peer is missing
        missing_pieces = [i for i in range(self.torrent.total_pieces) if not peer.has_piece(i)]

        # If the peer has all pieces, return None
        if not missing_pieces:
            return None

        # Randomly select one of the missing pieces
        return random.choice(missing_pieces)

    def rarest_first(self, peer):
        """
        Selects the rarest piece that the given peer doesn't have.

        :param peer: The peer for which to select a piece.
        :return: The index of the selected piece, or None if no pieces are available.
        """
        # Count the occurrences of each piece among all peers
        piece_counts = Counter()
        for p in self.torrent.peers:
            for piece in p.pieces:
                piece_counts[piece] += 1

        # Ensure all pieces are in the counter with at least a count of 0
        for i in range(self.torrent.total_pieces):
            if i not in piece_counts:
                piece_counts[i] = 0

        # Identify pieces that the peer is missing
        missing_pieces = [i for i in range(self.torrent.total_pieces) if not peer.has_piece(i)]

        # If the peer has all pieces, return None
        if not missing_pieces:
            return None

        # Sort missing pieces by their rarity (least frequent first), and by piece index for tie-breaking
        rarest_pieces = sorted(missing_pieces, key=lambda piece: (piece_counts[piece], piece))

        # Return the rarest missing piece
        return rarest_pieces[0] if rarest_pieces else None
