
from generator.aiClient import AiClient



class TagsExtractor(AiClient):
    def __init__(self, model_name: str = "llama3"):
        super().__init__(model_name=model_name)
        self.tags = []

    def extract_tags(self, content: str):
        PROMPT = f"""
            You are a professional tech journalist and SEO strategist.

            Your task is to extract a precise, concise list of keywords or tags that best represent the core themes of the modern technology article below.

            Before finalising, internally consider multiple options and evaluate them based on:
            - Relevance to the actual content (avoid inferred or unrelated tags)
            - Inclusion of core technologies, tools, companies, and key industry terms
            - SEO value and search visibility
            - Clarity, conciseness, and suitability for tagging/blog categorisation
            - Use only terms actually present or strongly implied in the article
            - Avoid generic filler tags (e.g. "technology" or "software" unless specifically central)
            - Return only the essential, high-quality tags

            Output must be a single, comma-separated list, with no formatting, no explanation, and no extra characters. Keep it clean, sharp, and Code&Coffee-ready.

            Article:
            {content}

            [List of Tags Only]
            """

        # Generate tags and ensure they are a list
        raw_tags = self.generate(PROMPT)

        # Split and clean tags
        self.tags = [tag.strip() for tag in raw_tags.split(",") if tag.strip()]
        print(f"Tags extracted: {self.tags}")

        return self.tags
