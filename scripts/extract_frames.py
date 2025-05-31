import os
import sys
import cv2
import yt_dlp

DOWNLOAD_DIR = "downloads"
FRAMES_DIR = "frames"
FRAME_INTERVAL = 5  # in seconds

def download_video(url):
    print("[INFO] Downloading video...")

    # Create download directory if it doesn't exist
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])

    # Find the downloaded file
    files = os.listdir(DOWNLOAD_DIR)
    video_files = [f for f in files if f.endswith(".mp4")]
    if not video_files:
        raise FileNotFoundError("[ERROR] Could not locate video file after download.")

    video_path = os.path.join(DOWNLOAD_DIR, video_files[0])
    print(f"[INFO] Download complete: {video_path}")
    return video_path

def extract_frames(video_path):
    print("[INFO] Extracting frames...")

    os.makedirs(FRAMES_DIR, exist_ok=True)
    vidcap = cv2.VideoCapture(video_path)

    if not vidcap.isOpened():
        print("[ERROR] Failed to open video file.")
        return

    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    interval = fps * FRAME_INTERVAL
    frame_count = 0
    saved_count = 0

    while True:
        success, image = vidcap.read()
        if not success:
            break
        if frame_count % interval == 0:
            frame_path = os.path.join(FRAMES_DIR, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_path, image)
            saved_count += 1
        frame_count += 1

    vidcap.release()
    print(f"[INFO] Extracted {saved_count} frames.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_frames.py <YouTube URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        video_file = download_video(url)
        extract_frames(video_file)
    except Exception as e:
        print(f"[ERROR] {e}")

# so that ocr_frames triggers after this 
import subprocess

# ... existing code ...

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_frames.py <YouTube URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        video_file = download_video(url)
        extract_frames(video_file)

        #  Trigger OCR script
        print("[INFO] Triggering OCR script...")
        subprocess.run(["python", os.path.join("scripts", "ocr_framess.py")])

    except Exception as e:
        print(f"[ERROR] {e}")
