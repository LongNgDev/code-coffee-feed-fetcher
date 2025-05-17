from generator.aiClient import AiClient
from articles.News import Article

class ContentGenerator(AiClient):
    def __init__(self, model_name: str = "llma3", article: Article = None):
        super().__init__(model_name=model_name)
        self.article = article or Article()
        
    def generate_title(self, content:str):
        title = None
        
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

            Return only the single, best headline as h1 component in HTML — no quotation marks, no explanation, and no extra formatting.
            
            [Strictly Follow the Rule above]

            Article:
            {content}

            [Title Only]

            """

        # Generate Title and return in HTML format
        try:
            title = self.generate(PROMPT) or None
            
            clean_title_html = self.clean_html_response(title)

            self.article.set_title(clean_title_html)

            return clean_title_html

        except Exception as e:
            print(f"❌ Error occured during generate Title: {e}")
        
        return title

    def generate_content(self, content:str):
        """Generate content based on the provided prompt."""

        aiContent = None

        PROMPT = f"""
            You are a professional tech journalist and SEO expert writing for Code&Coffee — a cozy, smart, and trustworthy technology blog designed for curious readers who value clarity, depth, and narrative storytelling.

            Your task:
            Write a high-quality, SEO-optimised article body in clean, valid raw HTML — ready for direct web embedding. The tone should be intelligent, friendly, slightly warm, and conversational — like a tech-savvy barista walking readers through a breaking story with insight and charm.

            Content Strategy & Flow:
            - Total word count: approximately 700–900 words
            - Internally evaluate multiple narrative flows; pick the most compelling one
            - Start with:
                • A single <h2> subheading (do NOT repeat the article title)
                • A short <p> introduction that sets the context and draws the reader in
            - Clearly explain:
                • The core news angle and its broader significance
                • The timeline of key events and regulatory backdrop (if applicable)
                • Who is involved — individuals, companies, technologies, or transactions
            - Use one <p> tag per paragraph — each paragraph should express a distinct idea
            - Use <h3> tags to introduce 2–4 clear subsections within the article body when appropriate 
            - Ensure smooth transitions between paragraphs (journalistic rhythm and logic)
            - Maintain a smart, friendly, journalistic tone with action verbs and clarity
            - End with a conclusion that reinforces the topic using SEO-relevant phrases like:
                • <strong>AI startup</strong>
                • <strong>regulatory compliance</strong>
                • <strong>tech investment</strong>

            SEO & Emphasis Formatting Rules:

            - <strong> — Use to highlight:
                • Proper nouns (e.g. <strong>OpenAI</strong>, <strong>ChatGPT</strong>)
                • Key figures and dates (e.g. <strong>$75 million</strong>, <strong>2023</strong>)
                • Industry terms (e.g. <strong>generative AI</strong>, <strong>machine learning</strong>)
                • Legal/policy terms (e.g. <strong>CFIUS</strong>, <strong>AI Act</strong>)

            - <em> — Use for nuance, tone, or contrast:
                • Irony, uncertainty, tone (e.g. <em>“wow, actions have consequences?”</em>)
                • Doubt or soft phrasing (e.g. <em>allegedly</em>, <em>on the other hand</em>)

            - <strong><em>...</em></strong> — Use for phrases that are emotionally or politically critical:
                • e.g. <strong><em>national security concern</em></strong>, <strong><em>massive investment risk</em></strong>

            Formatting & Output Constraints:

            - Return ONLY valid, clean HTML body content
            - Use ONLY the following tags: <h2>, <p>, <strong>, <em>, <strong><em>
            - Begin with a single <h2> tag
            - Use one <p> tag per paragraph (do not combine or skip)
            - Do NOT use markdown, triple backticks, syntax hints, or code formatting
            - Do NOT bold or italicise entire paragraphs or technical filler
            - Do NOT include meta tags, descriptions, editor notes, or extra explanation

            Below is the article source content. Apply all rules above when formatting:

            [BEGIN ARTICLE SOURCE]
            {content}
            [END ARTICLE SOURCE]

            [Output: HTML Body Content Only — Begin with <h2>]
            """




        # Generate content and return in HTML format
        try:
            aiContent = self.generate(PROMPT) or None

            # Check if the AI content is empty or None
            if not aiContent:
                print("❌ No content generated.")
                return None

            # Clean up any markdown or newline artifacts from the output
            cleaned_content_html = self.clean_html_response(aiContent)

            self.article.set_content(cleaned_content_html)

        except Exception as e:
            print(f"❌ Error occured during generate Content: {e}")
        
        return cleaned_content_html
        
    def clean_html_response(self, raw:str = ""):
        if raw == "":
            return raw
        
        cleaned = raw.strip()

        # Step 1: Remove triple backticks + optional 'html' tag
        if cleaned.startswith("```html"):
            cleaned = cleaned[7:].strip()
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:].strip()

        if cleaned.endswith("```"):
            cleaned = cleaned[:-3].strip()

        # Step 2: Replace literal \n with actual line breaks (only if needed)
        # Optional — for double-escaped LLM outputs
        cleaned = cleaned.replace('\\n', '')  # Unescape \n
        cleaned = cleaned.replace('\n\n', '')  # Clean up double newlines
        cleaned = cleaned.replace('\n', '')

        return cleaned.strip()
        
    def get_article(self):
        return self.article
        
      

if __name__ == "__main__":
    ARTICLE = """Manus AI is one of the hottest AI agent startups around, recently raising $75 million at a half-billion-dollar valuation in a round led by Benchmark.

    But two unnamed sources told Semafor that the investment is now under review by the U.S. Treasury Department over its compliance with 2023 restrictions on investing in Chinese companies.

    Benchmark’s lawyers cleared the investment because Manus isn’t technically developing its own AI models, but is instead a “wrapper” around existing ones, Semafor reported.

    Those lawyers also concluded Manus is not China-based since it’s incorporated in the Cayman Islands. (That’s a common structure used by Chinese companies, like Alibaba , to access foreign capital.)

    Benchmark has attracted criticism for its Manus investment from Founders Fund partner Delian Asparouhov, who posted on X “wow, actions have consequences?”.
    """

    
    client = ContentGenerator("phi4")
    # title = client.generate_title(ARTICLE)
    content = client.generate_content(ARTICLE)
    print(client.get_article().to_dict())

    # print(content)
    client.close()