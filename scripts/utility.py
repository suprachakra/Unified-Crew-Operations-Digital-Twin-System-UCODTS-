import os
import sys

def get_env_variable(name, default=None):
    """Retrieve an environment variable or return default if not set."""
    value = os.getenv(name)
    if value is None:
        if default is not None:
            return default
        print(f"Error: Environment variable {name} is not set.", file=sys.stderr)
        sys.exit(1)
    return value

def print_banner(message: str):
    """Print a formatted banner message."""
    banner = "=" * len(message)
    print(banner)
    print(message)
    print(banner)

if __name__ == "__main__":
    print_banner("Utility Script Running")
    var = get_env_variable("TEST_VAR", "default_value")
    print(f"TEST_VAR: {var}")
