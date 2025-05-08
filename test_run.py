from extractor.contentExtractor import ContentExtractor
from extractor.factory import get_extractor_for_url


def main():
    # Import the function to be tested

    content_extractor = get_extractor_for_url("https://techcrunch.com/2025/05/05/apple-plans-to-split-iphone-18-launch-into-two-phases-in-2026/")

    # content_extractor = ContentExtractor("https://techcrunch.com/2025/05/05/apple-plans-to-split-iphone-18-launch-into-two-phases-in-2026/")
    content = content_extractor.extract_content()
    print(content)


if __name__ == "__main__":
    main()
