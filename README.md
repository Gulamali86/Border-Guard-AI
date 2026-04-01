🛡️ BorderGuard AI: Integrated Intrusion Detection System
BorderGuard AI is a multi-modal security framework designed to protect critical border infrastructure. It combines Unsupervised Machine Learning for sensor anomaly detection with Computer Vision for real-time surveillance monitoring.

🚀 Key Features
Sensor Anomaly Detection: Uses an Isolation Forest model to identify irregularities in flow, level, and pressure sensors across 6 distinct security zones.

Visual Intrusion Detection: Leverages YOLOv8 (You Only Look Once) to detect humans, vehicles, and unauthorized objects in surveillance footage.

Unified Dashboard: A single-interface Gradio application deployed on Hugging Face for real-time system analysis.

Stealth Processing: Optimized to process video data and output detection logs without requiring constant high-bandwidth playback.

🛠️ Tech Stack
Language: Python 3.9+

Machine Learning: Scikit-Learn (Isolation Forest)

Computer Vision: Ultralytics (YOLOv8)

Web Framework: Gradio / Streamlit

Data Handling: Pandas, NumPy

Deployment: Hugging Face Spaces

📊 Dataset Information
The project utilizes the Border Sensor Dataset, which includes:

Timestamped Sensor Data: 54,000+ rows of flow, pressure, and level readings.

Attack Labels: Data categorized into "Normal" and "Attack" states across 6 stages of an intrusion attempt.

Geospatial Data: Simulated Latitude and Longitude coordinates for mapping high-risk zones.

💻 Installation & Usage

Install Dependencies:

Bash
pip install -r requirements.txt
Run the App:

Bash
python app.py
📂 Project Structure
Plaintext
├── app.py              # Main Gradio application
├── requirements.txt    # List of required Python libraries
├── attack.csv          # Sample sensor dataset
├── yolov8n.pt          # Pre-trained YOLOv8 Nano weights
└── README.md           # Project documentation
🛡️ License
This project is licensed under the MIT License - see the LICENSE file for details.
