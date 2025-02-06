import os
import json
from dotenv import load_dotenv
from pathlib import Path

def load_configuration():
    env_path = Path(__file__).parent.parent.parent / "app.env"
    print(f"Loading .env from: {env_path}")
    print(f"File exists: {env_path.exists()}")
    
    load_dotenv(dotenv_path=env_path)
    
    token = os.getenv("DISCORD_TOKEN")
    print(f"Token loaded: {token[:20]}..." if token else "Token not found!")
    
    config = {
        "token": token,
        "prefix": os.getenv("DISCORD_PREFIX"),
        "database": {
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_DATABASE")
        }
    }
    
    print(f"Prefix loaded: {config['prefix']}")
    print(f"Database host loaded: {config['database']['host']}")
    print(f"Database user loaded: {config['database']['user']}")
    print(f"Database password loaded: {'*' * len(config['database']['password']) if config['database']['password'] else 'Not found'}")
    print(f"Database name loaded: {config['database']['database']}")
    
    config_dir = Path(__file__).parent.parent.parent / "config"
    config_dir.mkdir(exist_ok=True)
    
    config_file = config_dir / "config.json"
    with open(config_file, "w") as f:
        json.dump(config, f, indent=4)
    
    return config

if __name__ == "__main__":
    load_configuration()
