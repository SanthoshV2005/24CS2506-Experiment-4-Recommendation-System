"""
Automated Video Demonstration Recorder and Screenshot Capture
for Experiment 4: Personalized Recommendation System
Student: Santhosh V (URK23CS1003)
"""

import os
import sys
import time
import subprocess
import threading
import ctypes
import win32gui
from PIL import ImageGrab

FFMPEG_PATH = r"C:\Users\Admin\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
EXP_DIR = r"D:\OllamaLab\Exp4_RecommendationSystem"
SCREENSHOT_DIR = os.path.join(EXP_DIR, "screenshots")
VIDEO_OUTPUT = r"D:\OllamaLab\Videos\Experiment_4_Recommendation_System.mp4"
STATUS_FILE = os.path.join(EXP_DIR, "status.txt")

def setup_desktop():
    user32 = ctypes.windll.user32
    h_default = user32.OpenDesktopW("default", 0, False, 0x10000000)
    user32.SetThreadDesktop(h_default)
    return user32

def record_video(stop_event, bbox=None):
    """Record screen frames and pipe to FFmpeg."""
    setup_desktop()
    width = 1536
    height = 864
    if bbox:
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]

    width = width if width % 2 == 0 else width - 1
    height = height if height % 2 == 0 else height - 1

    cmd = [
        FFMPEG_PATH, "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{width}x{height}",
        "-pix_fmt", "rgb24",
        "-r", "10",
        "-i", "-",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "ultrafast",
        VIDEO_OUTPUT
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    try:
        while not stop_event.is_set():
            img = ImageGrab.grab(bbox=bbox)
            if img.size != (width, height):
                img = img.resize((width, height))
            proc.stdin.write(img.tobytes())
            time.sleep(0.09)
    finally:
        try:
            proc.stdin.close()
            proc.wait(timeout=10)
        except Exception:
            proc.kill()

def capture_screenshot(hwnd, name):
    user32 = setup_desktop()
    user32.SetForegroundWindow(hwnd)
    time.sleep(0.4)
    rect = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox=rect)
    filepath = os.path.join(SCREENSHOT_DIR, name)
    img.save(filepath)
    print(f"[SCREENSHOT] Saved: {filepath} ({img.size[0]}x{img.size[1]})")

def get_status():
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            pass
    return ""

def main():
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(VIDEO_OUTPUT), exist_ok=True)
    if os.path.exists(STATUS_FILE):
        os.remove(STATUS_FILE)

    user32 = setup_desktop()

    print("[RECORDER] Launching CMD terminal running Exp 4 demo on Windows Desktop...")
    si = subprocess.STARTUPINFO()
    si.lpDesktop = r"WinSta0\default"

    win_title = "Exp4_RecommendationSystem_SanthoshV"
    proc = subprocess.Popen(
        ["cmd.exe", "/k", f"title {win_title} & color 0F & cd /d {EXP_DIR} & python demo_runner.py"],
        startupinfo=si,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    time.sleep(2)

    # Find Window
    hwnd_target = None
    for _ in range(20):
        def enum_cb(h, _):
            nonlocal hwnd_target
            if win_title in win32gui.GetWindowText(h):
                hwnd_target = h
        win32gui.EnumWindows(enum_cb, None)
        if hwnd_target:
            break
        time.sleep(0.5)

    if not hwnd_target:
        print("[ERROR] Could not find CMD window!")
        proc.terminate()
        return

    # Maximize window
    user32.ShowWindow(hwnd_target, 3) # SW_MAXIMIZE
    time.sleep(1)
    rect = win32gui.GetWindowRect(hwnd_target)
    print(f"[RECORDER] Window found and maximized. Rect: {rect}")

    # Start video recording thread
    stop_event = threading.Event()
    rec_thread = threading.Thread(target=record_video, args=(stop_event, rect))
    rec_thread.start()
    print("[RECORDER] Screen recording started...")

    captured_steps = set()
    step_mapping = {
        "step_1_ready": "01_main_menu.png",
        "step_2_ready": "02_user_profile.png",
        "step_4_ready": "03_preference_analysis.png",
        "step_5_ready": "04_prompt_generation.png",
        "step_6_ready": "05_generated_recommendations.png",
        "step_7_ready": "06_ranking_table.png",
        "step_8_ready": "07_explanations.png",
        "step_10_ready": "08_feedback_refinement.png",
        "step_11_ready": "09_intent_detection.png",
        "step_12_ready": "10_saved_recommendations.png",
    }

    try:
        start_time = time.time()
        while time.time() - start_time < 360:
            st = get_status()
            if st in step_mapping and st not in captured_steps:
                time.sleep(0.5)
                capture_screenshot(hwnd_target, step_mapping[st])
                captured_steps.add(st)
                print(f"[PROGRESS] Completed step capture: {st}")

            if st == "demo_completed":
                print("[RECORDER] Demo signaled completion!")
                time.sleep(3)
                break
            time.sleep(0.5)
    finally:
        print("[RECORDER] Stopping video recording...")
        stop_event.set()
        rec_thread.join(timeout=10)
        try:
            proc.terminate()
        except Exception:
            pass

    print("[SUCCESS] Experiment 4 video demonstration and screenshots recorded!")

if __name__ == "__main__":
    main()
