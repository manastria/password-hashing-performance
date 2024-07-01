# Password Hashing Performance Comparison

This repository contains a Python script to compare the performance of different hashing algorithms used for password security. The script demonstrates the speed and output differences between bcrypt, MD5, SHA-256, and SHA-3-256.

## Description

The script hashes a password multiple times using different algorithms and measures the time taken for each. It also displays the first few hashes to show the format and structure of the hashed outputs. This comparison helps in understanding the trade-offs between security and performance for each algorithm.

## Features

- Compare hashing algorithms: bcrypt, MD5, SHA-256, and SHA-3-256
- Measure and display the time taken for hashing
- Display the first few hash outputs for each algorithm
- Configurable number of iterations and display count

## Requirements

- Python 3.6 or higher
- `pipenv` for managing dependencies

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/manastria/password-hashing-performance.git
    cd password-hashing-performance
    ```

2. Install the required libraries using `pipenv`:
    ```bash
    pipenv install
    ```

3. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

4. Run the script:
    ```bash
    python hash_comparison.py
    ```

5. The script will display the time taken for hashing and the first few hashes for each algorithm.

## Configuration

You can adjust the following parameters in the script:

- `password`: The password to be hashed (default: `b"mon_mot_de_passe_tres_securise"`)
- `iterations`: The number of iterations for hashing (default: `1000`)
- `bcrypt_cost`: The cost factor for bcrypt (default: `12`)
- `display_hash_count`: The number of hashes to display (default: `5`)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


