import cmd
import random
import time
from BitTorrent.torrent import Torrent
from BitTorrent.peer import Peer
from BitTorrent.piece_selector import PieceSelector
from BitTorrent.choking_manager import ChokingManager


class TorrentCLI(cmd.Cmd):
    intro = 'Welcome to the BitTorrent simulation CLI. Type help or ? to list commands.\n'
    prompt = '(torrent) '

    def __init__(self):
        super().__init__()
        self.torrent = None
        self.peers = []
        self.piece_selector = None
        self.choking_manager = None

    def do_seed(self, arg):
        'Set the random seed for reproducibility: seed <seed_value>'
        try:
            seed_value = int(arg.strip())
            random.seed(seed_value)
            print(f'Random seed set to {seed_value}.')
        except ValueError:
            print("Please provide a valid integer seed value.")

    def do_init(self, arg):
        'Initialize the torrent with a specified number of pieces: init <total_pieces>'
        try:
            total_pieces = int(arg.strip())
            if total_pieces <= 0:
                print("Please provide a valid positive number of pieces.")
                return
            self.torrent = Torrent(total_pieces=total_pieces)
            self.peers = []
            self.piece_selector = PieceSelector(self.torrent)
            self.choking_manager = ChokingManager(self.torrent, unchoke_slots=3, optimistic_unchoke_interval=2)
            print(f'Torrent initialized with {total_pieces} pieces.')
        except ValueError:
            print("Please provide a valid number of pieces.")

    def do_add_peer(self, arg):
        'Add a peer to the torrent: add_peer <peer_id>'
        if self.torrent:
            peer_id = arg.strip()
            if not peer_id:
                print("Please provide a valid peer ID.")
                return
            new_peer = Peer(peer_id)
            self.torrent.add_peer(new_peer)
            self.peers.append(new_peer)
        else:
            print("Please initialize the torrent first using 'init' command.")

    def do_distribute_pieces(self, arg):
        'Distribute initial pieces to peers randomly: distribute_pieces'
        if self.torrent and self.peers:
            for peer in self.peers:
                for _ in range(random.randint(1, 3)):
                    piece = random.randint(0, self.torrent.total_pieces - 1)
                    peer.add_piece(piece)
            self.do_print_state("")
        else:
            print("Please initialize the torrent and add peers first.")

    def do_choke_management(self, arg):
        'Perform choking management and piece selection: choke_management'
        if self.torrent and self.peers:
            for step in range(5):
                print(f"\n--- Step {step + 1} ---")

                # Manage choking
                self.choking_manager.manage_choking()

                # Each peer selects a piece to download
                for peer in self.peers:
                    if not peer.is_choked:
                        if peer.is_interested:
                            selected_piece = self.piece_selector.rarest_first(peer)
                            if selected_piece is not None:
                                peer.add_piece(selected_piece)
                                self.torrent.broadcast_piece(peer.peer_id, selected_piece)
                        else:
                            selected_piece = self.piece_selector.random_first(peer)
                            if selected_piece is not None:
                                peer.express_interest()

                # Print the state after each step
                self.do_print_state("")

                # Wait for a moment before the next round
                time.sleep(1)
        else:
            print("Please initialize the torrent, add peers, and distribute pieces first.")

    def do_print_state(self, arg):
        'Print the current state of the torrent: print_state'
        if self.torrent:
            print("\n--- Current State of Torrent ---")
            for peer in self.torrent.peers:
                print(peer)
            print("\n")
        else:
            print("Please initialize the torrent first.")

    def do_run_file(self, arg):
        'Run commands from a file: run_file <file_path>'
        file_path = arg.strip()
        try:
            with open(file_path, 'r') as file:
                commands = file.readlines()
                for command in commands:
                    self.onecmd(command.strip())
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def do_quit(self, arg):
        'Quit the simulation: quit'
        print('Thank you for using the BitTorrent simulation CLI.')
        return True


if __name__ == '__main__':
    TorrentCLI().cmdloop()
