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


## Authors

- [@FabioDevIsTyping](https://www.github.com/octokatherine)
