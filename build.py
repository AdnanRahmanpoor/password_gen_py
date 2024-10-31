import subprocess
import sys
import os
from build_config import get_pyinstaller_config

def build_executable():
    # Get configuration
    config, platform = get_pyinstaller_config()
    
    # Construct PyInstaller command
    cmd = ['pyinstaller']
    
    # Add configuration options
    cmd.extend(['--name', config['name']])
    if config.get('icon'):
        cmd.extend(['--icon', config['icon']])
    if config.get('noconsole'):
        cmd.append('--noconsole')
    if config.get('onefile'):
        cmd.append('--onefile')
    if config.get('clean'):
        cmd.append('--clean')
    
    # Add hidden imports
    for import_name in config.get('hidden_imports', []):
        cmd.extend(['--hidden-import', import_name])
    
    # Add main script
    cmd.append(config['scripts'][0])
    
    # Execute build command
    print(f"Building executable for {platform}...")
    subprocess.run(cmd, check=True)
    print("Build completed successfully!")

if __name__ == "__main__":
    build_executable()