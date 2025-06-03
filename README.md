# Code Extractor

A Spring Boot application that extracts code snippets from YouTube video lectures.  
It downloads the video, extracts frames, runs OCR (Optical Character Recognition) on each frame, and returns the code found in the video.

---

##  Features

- Download videos from YouTube via URL
- Extract frames from video lectures
- Run OCR to detect and extract code snippets
- Simple web interface and REST API
- Modular design: Java (Spring Boot) backend, Python scripts for video and OCR processing

---


## 📦 Installation

### Prerequisites

- Java 17+ (or compatible with your Spring Boot version)
- Maven
- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to PATH
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading

### Steps

1. **Clone the repository**
    ```
    git clone https://github.com/HarshitS17/Code-Extractor.git
    cd Code-Extractor
    ```

2. **Install Python dependencies**
    ```
    pip install -r scripts/requirements.txt
    ```

3. **Build the Spring Boot application**
    ```
    mvn clean install
    ```

---

## 🛠 Usage

### Start the backend


### Access the web interface

Open [http://localhost:8080](http://localhost:8080) in your browser.

### API Usage

Send a POST request to `/extract` with the YouTube video URL in the request body.

---

##  Project Structure

Code-Extractor/
├── src/ # Java source code (Spring Boot)
│ └── main/
│ ├── java/
│ └── resources/
├── scripts/ # Python scripts for video processing and OCR
│ ├── download_video.py
│ ├── extract_frames.py
│ ├── ocr_code.py
│ └── requirements.txt
├── pom.xml # Maven dependencies
├── README.md # This file
└── ...


---

##  Contributing

Contributions are welcome!  
- Please open an issue for suggestions or bug reports.
- Fork the repo and submit a pull request for improvements.

---



##  Contact

Maintained by [HarshitS17](https://github.com/HarshitS17).  
For questions, open an issue or email: your.email@example.com

---

##  TODO

- [ ] Improve OCR accuracy and filtering of code
- [ ] Add support for more video platforms (e.g., Vimeo)
- [ ] Enhance the frontend UI/UX
- [ ] Add code syntax highlighting in results
- [ ] Dockerize the application for easier deployment

---