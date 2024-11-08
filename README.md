
# X-Platform Analyzer

**X-Platform Analyzer** is a Python-based application designed to analyze and visualize social media accounts on the X platform (formerly known as Twitter). The application securely manages API credentials, performs authentication, and will eventually support cross-platform functionality for desktop and mobile environments.

---

## Features
- **Secure API Authentication**: Uses the `tweepy` library to authenticate with the X platform, while keeping API credentials encrypted for security.
- **Encryption & Decryption**: Employs the `cryptography` library to encrypt and securely handle API keys and tokens.
- **Cross-Platform Compatibility**: Future plans to make the application available on Windows, MacOS, Linux, Android, and iOS.
- **Data Analysis & Visualization**: (To be implemented) Analyze and visualize user connections and engagement on the X platform.

---

## Project Structure
- `app_main.py`: Main script to authenticate and connect to the X platform using encrypted credentials.
- `config_loader.py`: Loads and decrypts API credentials from an encrypted configuration file.
- `internal.conf`: Encrypted configuration file containing the API credentials.
- `encrypt_credentials.py`: Script to encrypt API credentials (added to `.gitignore` to avoid exposure).
- `DecryptionTest.py`: Script to test the decryption process (added to `.gitignore` to avoid exposure).
- `.gitignore`: Specifies files and directories to be ignored by Git.

---

## Setup and Installation
### Prerequisites
- **Python**: Make sure Python 3.6+ is installed on your system.
- **Virtual Environment**: It's recommended to use a virtual environment for dependency management.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/X-Platform-Analyzer.git
   cd X-Platform-Analyzer
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   ```
3. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Make sure to generate a `requirements.txt` file by running `pip freeze > requirements.txt`)*

5. **Set the Encryption Key**:
   - On **Windows**:
     ```bash
     set ENCRYPTION_KEY=your_encryption_key_here
     ```
   - On **MacOS/Linux**:
     ```bash
     export ENCRYPTION_KEY=your_encryption_key_here
     ```
   Replace `your_encryption_key_here` with the actual encryption key generated using `encrypt_credentials.py`.

---

## Usage
1. **Run the Main Script**:
   ```bash
   python app_main.py
   ```
   This will authenticate with the X platform and display the authentication status.

2. **Encrypting API Credentials**:
   - Use `encrypt_credentials.py` to encrypt your API keys and tokens. Make sure this script is not shared or committed.

3. **Testing Decryption**:
   - Use `DecryptionTest.py` to verify that your credentials are correctly decrypted.

---

## Future Development
- **Data Analysis**: Implement functionality to analyze and extract insights from user data on the X platform.
- **Graphical Visualization**: Add data visualization features using libraries like `matplotlib` or `networkx`.
- **Cross-Platform Frontend**: Develop a user-friendly frontend for desktop and mobile platforms.

---

## Security Considerations
- **Sensitive Information**: Ensure that the `ENCRYPTION_KEY` is stored securely and not hard-coded in the source code.
- **`.gitignore`**: Sensitive scripts (`encrypt_credentials.py`, `DecryptionTest.py`) and configuration files are listed in `.gitignore` to prevent accidental exposure.

---

## Contributing
Feel free to contribute by submitting issues or pull requests. Please ensure all new features are thoroughly tested and documented.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments
- **tweepy**: For simplifying interaction with the X platform API.
- **cryptography**: For providing robust encryption and decryption capabilities.
- **Contributors**: Thanks to all contributors who make this project better.
