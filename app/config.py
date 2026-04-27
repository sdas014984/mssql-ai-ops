import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        # --- Claude ---
        self.CLAUDE_API_KEY = self.get_env("CLAUDE_API_KEY")

        # --- Database ---
        self.DB_CONN = self.get_env("DB_CONN")

        # --- App ---
        self.APP_ENV = os.getenv("APP_ENV", "dev")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

        # --- Safety Controls (VERY IMPORTANT for auto-fix) ---
        self.AUTO_FIX_ENABLED = os.getenv("AUTO_FIX_ENABLED", "false").lower() == "true"
        self.ALLOWED_ACTIONS = os.getenv(
            "ALLOWED_ACTIONS",
            "kill_session"
        ).split(",")

    def get_env(self, key):
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Missing required environment variable: {key}")
        return value


settings = Settings()