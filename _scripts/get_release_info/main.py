import os
from pathlib import Path

from dotenv import load_dotenv
import httpx

load_dotenv()

current_dir = Path(__file__).parent
query_get_last_release_assets = (current_dir / "getLatestReleaseAssets.graphql").read_text()
url = "https://api.github.com/graphql"

repo_root_dir = current_dir.parent.parent
assert (repo_root_dir / ".git").exists()
output_file = repo_root_dir / "_data/release_assets.json"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def main():
    response = httpx.post(
        url,
        json={
            "query": query_get_last_release_assets,
            "variables": {
                "owner": "dfint",
                "name": "installer",
                "first": 2,
            }
        },
        follow_redirects=True,
        headers={"Authorization": f"Bearer {GITHUB_TOKEN}"},
        timeout=httpx.Timeout(60)
    )
    response.raise_for_status()

    response_json = response.json()
    assets = response_json["data"]["repository"]["latestRelease"]["releaseAssets"]["nodes"]
    for asset in assets:
        print(f"{asset['name']}: {asset['downloadUrl']}")


if __name__ == "__main__":
    main()
