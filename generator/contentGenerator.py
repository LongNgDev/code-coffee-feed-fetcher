from generator.aiClient import AiClient
from articles.Article import Article

class ContentGenerator(AiClient):
    def __init__(self, model_name: str = "llma3"):
        super().__init__(model_name=model_name)
        self.article = Article()
        
    def generate_title(self, content:str = ""):

        
        PROMPT = f"""
            You are a professional tech journalist and SEO expert.

            Your task is to write a single, catchy, and SEO-optimised headline for a modern technology news article, based on the article below.

            Before writing, consider multiple headline options internally. Evaluate them based on:
            - Character length (under 70)
            - Clarity and news value
            - SEO strength for search visibility
            - Must include relevant keywords naturally
            - Must clearly express the article’s main topic or angle
            - Use strong action words or curiosity hooks if appropriate
            - Must be engaging, newsy, and journalistic in tone
            - Keep the tone informative, but slightly conversational to fit the Code&Coffee blog audience — friendly, smart, and chill
            - Prioritisation of any available statistics or figures (e.g. investment amounts, review dates)

            Return only the single, best headline as plain text — no quotation marks, no explanation, and no extra formatting. [Strictly Follow the Rule above]

            Article:
            {content}

            [Title Only]

            """

        try:
            title = self.generate(PROMPT)

            if title is not None:
                print(f"title: {title}")
                self.article.set_title(title)
                print(f"article:{self.article.get_title()}")

        except Exception as e:
            print(f"❌ Error occured during generate Title: {e}")
        
        return title

    def generate_content(self, content:str = "") -> str:
        """Generate content based on the provided pro mpt."""
        PROMPT = f"""
            You are a professional tech journalist and SEO expert.

            Your task is to write clear, informative, and SEO-optimised body content for a modern technology news article, based on the source below.

            Before writing, consider multiple narrative flows internally and select the most effective structure based on the following:

            - Total word count should be approximately 700–900 words
            - Begin with a short, engaging introduction that sets the context
            - Clearly explain the news angle and timeline of events
            - Use strong, relevant keywords naturally within the flow of the article
            - Prioritise and highlight any key statistics, figures, or notable entities (e.g. investment amounts, review details, company names)
            - Maintain clarity, newsworthiness, and audience relevance
            - Use concise paragraphs with smooth transitions
            - Apply a journalistic tone with action verbs and curiosity hooks where suitable
            - Keep the writing smart, friendly, and slightly conversational to match Code&Coffee’s cozy yet professional brand voice
            - Ensure the conclusion reinforces the main topic by naturally including related terms to strengthen SEO and semantic relevance


            Important:
            - Return only the full article body content
            - Do not include a headline, quotation marks, meta descriptions, or any formatting
            - Do not explain what you’re doing — return only the final article as plain text

            [BEGIN ARTICLE SOURCE]
            {content}
            [END ARTICLE SOURCE]

            [Write Body Content Only — No Headline]
            """


        try:
            aiContent = self.generate(PROMPT)

        except Exception as e:
            print(f"❌ Error occured during generate Title: {e}")
        
        return aiContent
      

if __name__ == "__main__":
    ARTICLE = """Manus AI is one of the hottest AI agent startups around, recently raising $75 million at a half-billion-dollar valuation in a round led by Benchmark.

    But two unnamed sources told Semafor that the investment is now under review by the U.S. Treasury Department over its compliance with 2023 restrictions on investing in Chinese companies.

    Benchmark’s lawyers cleared the investment because Manus isn’t technically developing its own AI models, but is instead a “wrapper” around existing ones, Semafor reported.

    Those lawyers also concluded Manus is not China-based since it’s incorporated in the Cayman Islands. (That’s a common structure used by Chinese companies, like Alibaba , to access foreign capital.)

    Benchmark has attracted criticism for its Manus investment from Founders Fund partner Delian Asparouhov, who posted on X “wow, actions have consequences?”.
    """


    client = ContentGenerator("phi4")

    content = client.generate_content(ARTICLE)
    print(content)
    client.close()