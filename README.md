# Barcode API with FastAPI

A simple    , supporting multiple formats (e.g., EAN, Code128).

---

## 🚀 Getting Started

These instructions will guide you through setting up and running the project locally on **Windows** and **Unix**.

---

### 💻 Prerequisites

- **Python 3.7+** (Ensure Python is added to your PATH)
- **Pip** (Python package manager)

---

## 🪟 Setup on Windows

1. **Install Python** (if not already installed):
   - Download Python from [python.org](https://www.python.org/downloads/).
   - Make sure to **check "Add Python to PATH"** during installation.

2. **Clone or Extract the Project**:
   - Download or clone the ZIP file of this project and extract it to your preferred directory.

3. **Open VSCode**:
   - Open **VSCode** and the extracted folder using `File -> Open Folder`.

4. **Set Up Virtual Environment (optional but recommended)**:
   Open the **VSCode terminal** (`Ctrl + ~`) and run the following commands:
   
   ```bash
   python -m venv myenv
   .\myenv\Scripts\Activate
   ```

5. **Install Required Dependencies**:
   Install the required dependencies using `pip`:
   
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the FastAPI Server**:
   In the **VSCode terminal**, run the following command to start the FastAPI server:
   
   ```bash
   uvicorn app.main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

---

## 🐧 Setup on Unix (Linux/macOS)

1. **Install Python** (if not already installed):
   - For Linux: Run `sudo apt-get install python3 python3-pip` (or use your package manager).
   - For macOS: Use Homebrew: `brew install python`.

2. **Clone or Extract the Project**:
   - Download or clone the ZIP file of this project and extract it to your preferred directory.

3. **Open Terminal** and navigate to the project folder.

4. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

5. **Install Required Dependencies**:
   Install the required dependencies using `pip`:
   
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the FastAPI Server**:
   In the terminal, run the following command:
   
   ```bash
   uvicorn app.main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

---

## 🌍 Test the API

1. **Open the API in a Browser**:
   - Open your browser and navigate to `http://127.0.0.1:8000/barcode?data=1234567890123`.
   - This should return a PNG image of the barcode.

2. **Testing with curl (optional)**:
   You can also test the API using `curl` from the terminal:
   
   ```bash
   curl http://127.0.0.1:8000/barcode?data=1234567890123 --output barcode.png
   ```

   This will save the barcode image as `barcode.png` in your current directory.

---

## 🚀 Running the API in Production (Optional)

You can deploy this API to platforms like **Render**, **Railway**, or **Fly.io**. If you'd like to run the app in production mode:

1. Use **Docker** (optional) for containerization.
2. Follow platform-specific deployment guides:
   - [Render Deployment Guide](https://render.com/docs/deploy-fastapi)
   - [Railway Deployment Guide](https://railway.app/docs/deploy)
   - [Fly.io Deployment Guide](https://fly.io/docs/getting-started/)

---

## 📚 Additional Information

- **Supported Barcode Formats**: EAN-13, EAN-8, Code128, etc.
- **Documentation**: The FastAPI app provides interactive docs at `http://127.0.0.1:8000/docs`.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
