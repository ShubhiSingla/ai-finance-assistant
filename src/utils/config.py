# Config - loads and exposes application configuration from config.yaml and .env
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

_CONFIG_PATH = Path(__file__).parents[2] / "config.yaml"


def load_config() -> dict:
    """Load and return the full config.yaml as a dict."""
    with open(_CONFIG_PATH) as f:
        return yaml.safe_load(f)


# Convenience accessors
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
NEWS_API_KEY: str = os.getenv("NEWS_API_KEY", "")
VECTOR_STORE_PATH: str = os.getenv("VECTOR_STORE_PATH", "data/vector_store")

config: dict = load_config()
