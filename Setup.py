import os
import sys
from pathlib import Path
import subprocess
import ctypes
import time

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Re-run the script with administrator privileges."""
    script = sys.executable
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", script, params, None, 1)

if not is_admin():
    print("Administrator privileges required to create symlinks. Re-running as administrator...")
    time.sleep(3)
    run_as_admin()
    sys.exit()

# Set working directory to script location
script_dir = Path(__file__).parent
os.chdir(script_dir)

# Create the required folders and symlinks
server_dir = script_dir / "Server"
folders = ["world", "superflat", "temporary"]

for folder in folders:
    folder_path = server_dir / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    symlink_path = folder_path / "datapacks"
    target_path = Path("..") / ".." / "datapacks"
    if not symlink_path.exists():
        symlink_path.symlink_to(target_path, target_is_directory=True)
        print(f"Created symlink: {symlink_path} -> {target_path}")
    else:
        print(f"Symlink already exists: {symlink_path}")

input("Setup complete. Press Enter to exit...")