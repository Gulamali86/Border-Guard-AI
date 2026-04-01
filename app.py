import gradio as gr
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from ultralytics import YOLO
import os

# Load YOLO model
try:
    model = YOLO("yolov8n.pt")
except Exception as e:
    print(f"Error loading model: {e}")

def start_analysis(csv_file, video_file):
    report = "--- SYSTEM ANALYSIS REPORT ---\n\n"
    processed_video_path = None
    
    # --- Part 1: CSV SAFETY CHECK ---
    if csv_file is not None:
        try:
            df = pd.read_csv(csv_file.name)
            # Find only numbers for the AI to read
            numeric_cols = df.select_dtypes(include=[np.number])
            
            if numeric_cols.empty:
                report += "📊 SENSOR ERROR: No numeric columns found in CSV.\n"
            else:
                iso = IsolationForest(contamination=0.05, random_state=42)
                df["anomaly"] = iso.fit_predict(numeric_cols)
                total_anomalies = len(df[df["anomaly"] == -1])
                report += f"📊 SENSOR STATUS: Success. Detected {total_anomalies} anomalies.\n"
        except Exception as e:
            report += f"📊 SENSOR ERROR: {str(e)}\n"
    else:
        report += "📊 SENSOR STATUS: No CSV uploaded.\n"

    # --- Part 2: VIDEO SAFETY CHECK ---
    if video_file is not None:
        try:
            # Process video and save it
            results = model.predict(source=video_file, save=True, conf=0.3)
            
            # Find where YOLO saved the video
            save_dir = results[0].save_dir
            files = os.listdir(save_dir)
            if files:
                # Get the first file in the directory
                processed_video_path = os.path.join(save_dir, files[0])
                report += "🎥 VIDEO STATUS: Success. Bounding boxes applied.\n"
            else:
                report += "🎥 VIDEO ERROR: YOLO failed to save the output file.\n"
        except Exception as e:
            report += f"🎥 VIDEO ERROR: {str(e)}\n"
    else:
        report += "🎥 VIDEO STATUS: No Video uploaded.\n"

    return report, processed_video_path

# --- UI Setup ---
with gr.Blocks() as demo:
    gr.Markdown("# 🛡️ BorderGuard AI: Final Solution")
    
    with gr.Row():
        with gr.Column():
            csv_in = gr.File(label="Upload CSV")
            vid_in = gr.Video(label="Upload MP4")
            btn = gr.Button("🚀 START ANALYSIS", variant="primary")
        
        with gr.Column():
            rep_out = gr.Textbox(label="Analysis Logs", lines=5)
            vid_out = gr.Video(label="Detection Results")

    btn.click(start_analysis, inputs=[csv_in, vid_in], outputs=[rep_out, vid_out])

demo.launch()