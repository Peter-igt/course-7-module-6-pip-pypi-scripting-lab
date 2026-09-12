
from datetime import datetime
import requests


def fetch_data():
    """Fetch a sample post from a public API."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(log_data):
    """Write log entries to a dated text file and return the filename."""
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename


def main():
    """Fetch API data and create the log file."""
    post = fetch_data()

    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched Post Title: {post.get('title', 'No title found')}"
    ]

    filename = generate_log(log_data)
    print(f"Log written to {filename}")


if __name__ == "__main__":
    main()
