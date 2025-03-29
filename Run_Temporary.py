import os
from pathlib import Path
import shutil
import subprocess

# Set working directory to script location
script_dir = Path(__file__).parent
os.chdir(script_dir)

# Update server.properties for temporary world
server_properties = os.path.join('Server', 'server.properties')
new_level_name = 'temporary'

with open(server_properties, 'r') as f:
    lines = f.readlines()

with open(server_properties, 'w') as f:
    for line in lines:
        if line.strip().startswith('level-name='):
            f.write(f'level-name={new_level_name}\n')
        elif line.strip().startswith('level-type='):
            f.write('level-type=normal\n')
        else:
            f.write(line)

# Clean temporary world directory while preserving datapacks
world_dir = os.path.join('Server', 'temporary')
if os.path.exists(world_dir):
    for item in os.listdir(world_dir):
        if item != 'datapacks':
            item_path = os.path.join(world_dir, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

# Start the server
subprocess.run(['run.bat'], shell=True, cwd='Server')