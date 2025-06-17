import requests
from bs4 import BeautifulSoup
import re
import os


class ThumbnailExtractor():
    def __init__(self, url: str, slug: str = None):
        self.url = url
        self.slug = slug
        self.header = {
            "User-Agent": "Mozilla/5.0"
        }

    def extract_thumbnail(self):
        response = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the image tag
        img_tag = soup.find("img", {"class": "wp-post-image"})
        if not img_tag:
            return "No thumbnail found"

        # Try to find the highest resolution from srcset
        srcset = img_tag.get("srcset", "")
        highest_url = None
        max_width = 0

        for item in srcset.split(","):
            parts = item.strip().split(" ")
            if len(parts) >= 2:
                url = parts[0]
                match = re.match(r"(\d+)w", parts[1])
                if match:
                    width = int(match.group(1))
                    if width > max_width:
                        max_width = width
                        highest_url = url

        # Fallback to src if no srcset found
        if not highest_url:
            highest_url = img_tag.get("src", "")

        if not highest_url.startswith("http"):
            highest_url = self.url + highest_url  # Just in case

        print(f"🌟 Thumbnail extracted: {highest_url}")
        return highest_url

    def download_thumbnail(self, save_folder="images"):
        img_url = self.extract_thumbnail()
        if not img_url.startswith("http"):
            print("❌ Invalid image URL.")
            return

        # Create the folder if it doesn't exist
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # Extract image name from URL
        filename = img_url.split("/")[-1].split("?")[0]

        print(f"📥 Downloading thumbnail: {img_url}")

        save_path = os.path.join(save_folder, self.slug + ".jpg" if self.slug else filename)

        # Download and save
        try:
            img_data = requests.get(img_url, headers=self.header).content
            with open(save_path, "wb") as f:
                f.write(img_data)
            print(f"📥 Image saved at: {save_path}")
        except Exception as e:
            print(f"❌ Failed to download: {e}")


if __name__ == "__main__":
    url = "https://techcrunch.com/2025/06/17/mastodon-updates-its-terms-to-prohibit-ai-model-training/"
    extractor = ThumbnailExtractor(url, slug="mastodon-update-thumbnail")
    extractor.download_thumbnail()
