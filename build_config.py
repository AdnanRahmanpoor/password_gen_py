import sys
from pathlib import Path

# Application information
APP_NAME = "PasswordGenerator"
APP_VERSION = "1.0.0"
MAIN_SCRIPT = "password_gen.py"  # Your main script file

# Icon paths for different platforms
ICON_PATH = {
    'Windows': 'icons/password.ico',
    'Darwin': 'icons/password.icns',
    'Linux': 'icons/password.png'
}

# PyInstaller configuration
def get_pyinstaller_config():
    # Determine OS-specific settings
    if sys.platform.startswith('win'):
        icon = ICON_PATH['Windows']
        platform = 'Windows'
    elif sys.platform.startswith('darwin'):
        icon = ICON_PATH['Darwin']
        platform = 'Darwin'
    else:
        icon = ICON_PATH['Linux']
        platform = 'Linux'
    
    # Base configuration
    config = {
        'name': APP_NAME,
        'scripts': [MAIN_SCRIPT],
        'hidden_imports': ['tkinter', 'pyperclip'],
        'noconsole': True,
        'onefile': True,
        'clean': True,
    }
    
    # Add icon if it exists
    if Path(icon).exists():
        config['icon'] = icon
    
    return config, platform

# Requirements file
requirements = """
tkinter
pyperclip
pyinstaller>=5.7.0
pillow  # for icon handling
"""

# Save requirements
with open('requirements.txt', 'w') as f:
    f.write(requirements.strip())