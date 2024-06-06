# File for managing configurations for the program
import os

# Server configurations
SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = int(os.getenv("SERVER_PORT"))

# Sandbox configurations
SANDBOX_TIMEOUT_S = int(os.getenv("SANDBOX_TIMEOUT_S"))
SANDBOX_CPU = int(os.getenv("SANDBOX_CPU"))
SANDBOX_MEMORY_MB = int(os.getenv("SANDBOX_MEMORY_MB"))

# Database configurations
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
