import os
from pathlib import Path
import subprocess

# Set working directory to script location
script_dir = Path(__file__).parent
os.chdir(script_dir)

# Update server.properties for superflat world
server_properties = Path('Server') / 'server.properties'
new_level_name = 'world'

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

# Start the server
subprocess.run(['run.bat'], shell=True, cwd='Server')