from pathlib import Path

# Project root directory
PROJECT_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_DIR / "data"

# Place below the paths to your project's data files
RAW_DATA = DATA_DIR / "example.csv"

# Place below the paths to your project's model files
MODELS_DIR = PROJECT_DIR / "models"

# Place below any other paths you find necessary
REPORTS_DIR = PROJECT_DIR / "reports"
IMAGES_DIR = REPORTS_DIR / "images"