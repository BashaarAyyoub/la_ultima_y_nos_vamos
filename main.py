import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.ui.gradio_app import lanzar_ui

if __name__ == "__main__":
    lanzar_ui()