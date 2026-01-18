import subprocess
import time
import os

# Path to your server script
SERVER_SCRIPT = os.path.join(os.getcwd(), "client.py")

def run_server_script():
    print("\n🚀 Running server script...")
    try:
        # Run the script as a separate process
        subprocess.run(["python", SERVER_SCRIPT], check=True)
        print("✅ Server script finished successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Server script failed with error: {e}")

print("⏱️ Scheduler started. Running 'client.py' every 10 minutes...")

while True:
    run_server_script()
    print("🕒 Waiting 10 minutes before next run...")
    time.sleep(600)  # 600 seconds = 10 minutes