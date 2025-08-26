import json
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
        headers={"Authorization": f"Bearer {GITHUB_TOKEN}"},
        timeout=httpx.Timeout(60)
    )
    response.raise_for_status()

    response_json = response.json()
    assets = response_json["data"]["repository"]["latestRelease"]["releaseAssets"]["nodes"]
    
    map_os_names = {
        "win": "windows",
        "lin": "linux",
    }

    result = {}
    for asset in assets:
        os_part = asset["name"].split("-")[2]
        os_name = map_os_names[os_part]
        print(f"{os_name}: {asset['downloadUrl']}")

        result[os_name] = {
            "name": asset["name"],
            "url": asset["downloadUrl"],
        }

    output_file.write_text(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
