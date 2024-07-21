Sure, here is the full version of the README with the deployment section included and properly formatted:

# Distributed Systems Project

This project is a part of the Distributed Systems course at UNICAM. It implements a BitTorrent client in Python. The project is organized in the `Project` directory.

## Project Structure

```
DistributedSystems/
│
├── Project/
│   ├── BitTorrent/
│   │   ├── __init__.py
│   │   ├── choking_manager.py
│   │   ├── peer.py
│   │   ├── piece_selector.py
│   │   └── torrent.py
│   │
│   ├── Tests/
│   │   ├── __init__.py
│   │   ├── test_choking_manager.py
│   │   ├── test_peer.py
│   │   ├── test_piece_selector.py
│   │   └── test_torrent.py
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── commands.txt
│   └── README.md
│
└── .gitignore
```

## Deployment

To get started with this project, follow these steps:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/FabioDevIsTyping/Distributed_Systems_UNICAM.git
   cd Distributed_Systems_UNICAM/Project
   ```

2. **Create a virtual environment:**

   It's recommended to use a virtual environment to manage your dependencies. You can create one using `venv`:

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - **Windows:**

     ```sh
     .\venv\Scripts\activate
     ```

   - **MacOS/Linux:**

     ```sh
     source venv/bin/activate
     ```

4. **Install the required packages:**

   Install the required packages listed in the `requirements.txt` file:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the main program, use the following command:

```sh
python main.py
```

## Dependencies

The project uses the following Python package:

- `cmd2`

You can install it using `pip` as mentioned in the installation steps.

### Available Commands

The BitTorrent project includes a set of commands that can be run from the command line interface to interact with the torrent client. Below are the descriptions of each command:

#### `add_peer`
- **Description**: Adds a new peer to the torrent client.
- **Usage**: `add_peer <peer_address>`
- **Example**: `add_peer 192.168.1.10:6881`
- **Details**: This command allows you to add a peer's address to the list of peers the torrent client can connect to for downloading and uploading pieces.

#### `choke_management`
- **Description**: Manages the choking and unchoking of peers.
- **Usage**: `choke_management`
- **Details**: This command triggers the choke management process, which involves deciding which peers to choke (restrict data transfer) and which to unchoke (allow data transfer) based on the implemented algorithm.

#### `distribute_pieces`
- **Description**: Distributes pieces of the torrent file to peers.
- **Usage**: `distribute_pieces`
- **Details**: This command is used to distribute pieces of the torrent file to connected peers, ensuring that the file is shared across the network.

#### `help`
- **Description**: Provides help information for available commands.
- **Usage**: `help <command>`
- **Example**: `help add_peer`
- **Details**: This command lists all available commands and provides detailed information on how to use a specific command when followed by the command name.

#### `init`
- **Description**: Initializes the torrent client.
- **Usage**: `init`
- **Details**: This command initializes the torrent client, setting up necessary configurations and preparing the client to start interacting with the torrent network.

#### `print_state`
- **Description**: Prints the current state of the torrent client.
- **Usage**: `print_state`
- **Details**: This command outputs the current state of the torrent client, including information about connected peers, downloaded pieces, and overall progress.

#### `quit`
- **Description**: Exits the torrent client.
- **Usage**: `quit`
- **Details**: This command stops the torrent client and exits the program.

#### `run_file`
- **Description**: Runs commands from a specified file.
- **Usage**: `run_file <filename>`
- **Example**: `run_file commands.txt`
- **Details**: This command executes a series of commands listed in a specified file, allowing for batch processing of commands.

#### `seed`
- **Description**: Starts seeding the torrent file.
- **Usage**: `seed`
- **Details**: This command starts the seeding process, allowing the torrent client to share the completed file with other peers in the network.

### How to Use the Commands

To use these commands, you can run the torrent client and enter the desired command at the prompt. For example, to add a peer, you would start the client and then type:

```sh
(torrent) add_peer 192.168.1.10:6881
```

You can also run a series of commands from a file by using the `run_file` command:

```sh
(torrent) run_file commands.txt
```

To get help on a specific command, simply type `help` followed by the command name:

```sh
(torrent) help add_peer
```

By using these commands, you can manage the torrent client effectively, adding peers, managing piece distribution, and controlling the client's state and behavior.
## Authors

- [@FabioDevIsTyping](https://www.github.com/octokatherine)
