# Tic Tac Toe

## Table of Contents
- [Repository](#Repository-Structure)
- [Installation](#Installation)
- [Usage](#Usage)
- [Notes](#Notes)

### Repository
```
├── README.md                     
├── requirements.txt    
│          
│
├── src/
│   ├── main.py
│   ├── queries.py
│   └── util.py
│
```

### Installation
1. Open the terminal and navigate into the source folder.
    ```bash
    $  cd tic-tac-toe
    ```
1. Create a virtual environment:
    ```bash
    $  python3 -m venv my-env
    ```
2. Activate the environment:
    ```bash
    $  source my-env/bin/activate
    ```
3. Install dependencies using requirements.txt:
    ```bash
    $  pip install -r requirements.txt
    ```

### Usage
1. Open the terminal, navigate into the source folder, and activate the virtual environment.
    ```bash
    $  cd tic-tac-toe
    $  source my-env/bin/activate
    ```
2. Run the application:
    ```bash
    $  python main.py
    ```
3. Enter your move (1-9), and then press 'return'.

### Notes
- The computer always goes first.
- The computer is 'X' and the user is 'O'.