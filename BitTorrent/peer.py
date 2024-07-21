class Peer:
    def __init__(self, peer_id):
        """
        Initializes a new peer.

        :param peer_id: A unique identifier for the peer.
        """
        self.peer_id = peer_id
        self.pieces = set()
        self.is_choked = True
        self.is_interested = False

    def choke(self):
        """
        Chokes this peer.
        """
        self.is_choked = True
        print(f"Peer {self.peer_id} has been choked.")

    def unchoke(self):
        """
        Unchokes this peer.
        """
        self.is_choked = False
        print(f"Peer {self.peer_id} has been unchoked.")

    def add_piece(self, piece_index):
        """
        Adds a piece to the peer's collection.

        :param piece_index: The index of the piece to add.
        """
        self.pieces.add(piece_index)
        print(f"Peer {self.peer_id} received piece {piece_index}.")

    def has_piece(self, piece_index):
        """
        Checks if the peer has a specific piece.

        :param piece_index: The index of the piece to check.
        :return: True if the peer has the piece, False otherwise.
        """
        return piece_index in self.pieces

    def express_interest(self):
        """
        Expresses interest in downloading pieces from another peer.
        """
        self.is_interested = True
        print(f"Peer {self.peer_id} is interested in downloading pieces.")

    def withdraw_interest(self):
        """
        Withdraws interest in downloading pieces from another peer.
        """
        self.is_interested = False
        print(f"Peer {self.peer_id} is no longer interested in downloading pieces.")

    def __str__(self):
        """
        Returns a string representation of the peer.
        """
        return f"Peer({self.peer_id}, Choked: {self.is_choked}, Interested: {self.is_interested}, Pieces: {sorted(self.pieces)})"